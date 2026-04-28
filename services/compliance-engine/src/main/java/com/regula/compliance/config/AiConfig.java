package com.regula.compliance.config;

import com.regula.compliance.advisor.CitationGuardianAdvisor;
import com.regula.compliance.advisor.TenantContextAdvisor;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AiConfig {

    @Bean
    public ChatClient.Builder chatClientBuilder(ChatModel chatModel) {
        // Here we pre-configure the builder with our custom advisors.
        // In a fully built application, we would also inject the VectorStore and use QuestionAnswerAdvisor.
        return ChatClient.builder(chatModel)
                .defaultAdvisors(
                        new TenantContextAdvisor(),
                        new CitationGuardianAdvisor()
                );
    }
}
