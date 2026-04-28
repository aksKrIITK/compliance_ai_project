package com.regula.compliance.advisor;

import org.springframework.ai.chat.client.advisor.api.AdvisedRequest;
import org.springframework.ai.chat.client.advisor.api.AdvisedResponse;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisorChain;
import reactor.core.publisher.Flux;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisorChain;

import java.util.HashMap;
import java.util.Map;

public class TenantContextAdvisor implements CallAroundAdvisor, StreamAroundAdvisor {

    private static final String ADVISOR_NAME = "TenantContextAdvisor";
    private static final int ORDER = -100;

    @Override
    public AdvisedResponse aroundCall(AdvisedRequest advisedRequest, CallAroundAdvisorChain chain) {
        // In a real application, extract from Spring Security Context
        String tenantId = "acme_eu"; 
        
        Map<String, Object> advisedContext = new HashMap<>(advisedRequest.advisorContext());
        advisedContext.put("tenant_id", tenantId);
        
        AdvisedRequest newRequest = AdvisedRequest.from(advisedRequest)
                .withAdvisorContext(advisedContext)
                .build();
                
        return chain.nextAroundCall(newRequest);
    }

    @Override
    public Flux<AdvisedResponse> aroundStream(AdvisedRequest advisedRequest, StreamAroundAdvisorChain chain) {
        String tenantId = "acme_eu"; 
        
        Map<String, Object> advisedContext = new HashMap<>(advisedRequest.advisorContext());
        advisedContext.put("tenant_id", tenantId);
        
        AdvisedRequest newRequest = AdvisedRequest.from(advisedRequest)
                .withAdvisorContext(advisedContext)
                .build();
                
        return chain.nextAroundStream(newRequest);
    }

    @Override
    public String getName() {
        return ADVISOR_NAME;
    }

    @Override
    public int getOrder() {
        return ORDER;
    }
}
