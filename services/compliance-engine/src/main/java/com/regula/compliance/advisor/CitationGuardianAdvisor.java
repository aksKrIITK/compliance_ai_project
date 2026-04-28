package com.regula.compliance.advisor;

import org.springframework.ai.chat.client.advisor.api.AdvisedRequest;
import org.springframework.ai.chat.client.advisor.api.AdvisedResponse;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisorChain;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisorChain;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.model.Generation;
import reactor.core.publisher.Flux;

import java.util.List;

public class CitationGuardianAdvisor implements CallAroundAdvisor, StreamAroundAdvisor {

    private static final String ADVISOR_NAME = "CitationGuardianAdvisor";
    private static final int ORDER = 0;

    @Override
    public AdvisedResponse aroundCall(AdvisedRequest advisedRequest, CallAroundAdvisorChain chain) {
        AdvisedResponse response = chain.nextAroundCall(advisedRequest);
        ChatResponse chatResponse = response.response();
        
        // This is a simplified check. In a real scenario, you would inspect the metadata
        // for actual citations provided by the RetrievalAugmentationAdvisor.
        boolean hasCitations = checkCitations(chatResponse);
        
        if (!hasCitations && chatResponse.getResult() != null) {
            String originalText = chatResponse.getResult().getOutput().getContent();
            String appendedText = originalText + "\n\n*Disclaimer: I could not verify this statement against your regulatory corpus.*";
            
            // Reconstruct the response with the disclaimer
            // Note: This is pseudocode for modifying the response, actual Spring AI API might differ slightly
            // based on the version.
        }
        
        return response;
    }

    @Override
    public Flux<AdvisedResponse> aroundStream(AdvisedRequest advisedRequest, StreamAroundAdvisorChain chain) {
        // For streaming, we might need to buffer or append at the end of the stream.
        return chain.nextAroundStream(advisedRequest);
    }

    @Override
    public String getName() {
        return ADVISOR_NAME;
    }

    @Override
    public int getOrder() {
        return ORDER;
    }

    private boolean checkCitations(ChatResponse chatResponse) {
        // Implement logic to check for Document citations in the response metadata
        return false;
    }
}
