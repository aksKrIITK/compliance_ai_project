package com.regula.ai;
import org.springframework.ai.chat.client.advisor.api.*;
import org.springframework.ai.chat.model.ChatResponse;
import reactor.core.publisher.Flux;
public class CitationGuardianAdvisor implements CallAroundAdvisor, StreamAroundAdvisor {
    @Override
    public AdvisedResponse aroundCall(AdvisedRequest advisedRequest, CallAroundAdvisorChain chain) {
        AdvisedResponse response = chain.nextCall(advisedRequest);
        return checkCitations(response);
    }
    @Override
    public Flux<AdvisedResponse> aroundStream(AdvisedRequest advisedRequest, StreamAroundAdvisorChain chain) {
        return chain.nextStream(advisedRequest).map(this::checkCitations);
    }
    private AdvisedResponse checkCitations(AdvisedResponse response) {
        ChatResponse chatResponse = response.response();
        if (chatResponse.getMetadata().get("source") == null) {
            // simplified: real would rebuild ChatResponse
        }
        return response;
    }
    @Override
    public String getName() { return "citation-guardian"; }
}
