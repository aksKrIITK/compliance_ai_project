package com.regula.ai;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
@Configuration
public class AiConfig {
    @Bean
    public TenantAwareVectorStore tenantAwareVectorStore(VectorStore actualVectorStore) {
        return new TenantAwareVectorStore(actualVectorStore);
    }
    @Bean
    public CitationGuardianAdvisor citationGuardianAdvisor() {
        return new CitationGuardianAdvisor();
    }
}
