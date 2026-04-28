package com.regula.ai.advisor;

import org.springframework.ai.chat.client.advisor.api.AdvisedRequest;
import org.springframework.ai.chat.client.advisor.api.AdvisedResponse;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisorChain;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisorChain;
import reactor.core.publisher.Flux;

public class PromptInjectionDetectionAdvisor implements CallAroundAdvisor, StreamAroundAdvisor {

    private static final String ADVISOR_NAME = "PromptInjectionDetectionAdvisor";
    private static final int ORDER = -1000; // Execute very early

    @Override
    public AdvisedResponse aroundCall(AdvisedRequest advisedRequest, CallAroundAdvisorChain chain) {
        validateRequest(advisedRequest);
        return chain.nextAroundCall(advisedRequest);
    }

    @Override
    public Flux<AdvisedResponse> aroundStream(AdvisedRequest advisedRequest, StreamAroundAdvisorChain chain) {
        validateRequest(advisedRequest);
        return chain.nextAroundStream(advisedRequest);
    }

    private void validateRequest(AdvisedRequest request) {
        String userText = request.userText();
        // A simple heuristic for prompt injection.
        // In production, this might call a fast, dedicated classification model.
        if (userText != null && (userText.toLowerCase().contains("ignore previous instructions") ||
                                 userText.toLowerCase().contains("system prompt"))) {
            throw new SecurityException("Potential prompt injection detected. Request rejected.");
        }
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
