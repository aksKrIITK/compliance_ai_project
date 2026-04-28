package com.regula.compliance.service;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;
import io.github.resilience4j.circuitbreaker.annotation.CircuitBreaker;

@Service
public class ComplianceQAService {

    private final ChatClient chatClient;

    public ComplianceQAService(ChatClient.Builder chatClientBuilder) {
        // In a real application, the defaultAdvisors would be configured in an AiConfig class,
        // injecting the VectorStore and custom advisors.
        this.chatClient = chatClientBuilder
            // .defaultAdvisors(
            //     new TenantContextAdvisor(),
            //     new QuestionAnswerAdvisor(vectorStore, SearchRequest.defaults().withTopK(10)),
            //     new CitationGuardianAdvisor()
            // )
            .build();
    }

    @CircuitBreaker(name = "llmCircuitBreaker", fallbackMethod = "fallbackAsk")
    public Flux<String> ask(String question, String conversationId) {
        return chatClient.prompt()
                .user(question)
                .stream()
                .content();
    }

    public Flux<String> fallbackAsk(String question, String conversationId, Throwable t) {
        return Flux.just("We are currently experiencing high load or the AI provider is unavailable. Please try again later. Error: " + t.getMessage());
    }
}
