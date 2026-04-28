package com.regula.security.filter;

import com.regula.security.context.TenantContextHolder;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;
import java.io.IOException;
import java.util.Collections;

public class JwtAuthenticationFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        String authHeader = request.getHeader("Authorization");

        if (authHeader != null && authHeader.startsWith("Bearer ")) {
            String token = authHeader.substring(7);
            try {
                // In a real application, parse JWT and validate signature
                // For demonstration, we simulate extracting tenant_id from the token
                String tenantId = extractTenantId(token);
                String userId = extractUserId(token);

                if (tenantId != null && userId != null) {
                    TenantContextHolder.setTenantId(tenantId);

                    UsernamePasswordAuthenticationToken authentication = new UsernamePasswordAuthenticationToken(
                            userId, null, Collections.emptyList()
                    );
                    SecurityContextHolder.getContext().setAuthentication(authentication);
                }
            } catch (Exception e) {
                // Ignore invalid tokens or log them
            }
        }

        try {
            filterChain.doFilter(request, response);
        } finally {
            TenantContextHolder.clear();
            SecurityContextHolder.clearContext();
        }
    }

    private String extractTenantId(String token) {
        // Mock implementation
        return "acme_eu";
    }

    private String extractUserId(String token) {
        // Mock implementation
        return "user123";
    }
}
