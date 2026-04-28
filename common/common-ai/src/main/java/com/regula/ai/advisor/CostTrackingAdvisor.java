package com.regula.ai.advisor;

import com.regula.security.context.TenantContextHolder;
import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.ai.chat.client.advisor.api.AdvisedRequest;
import org.springframework.ai.chat.client.advisor.api.AdvisedResponse;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.CallAroundAdvisorChain;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisor;
import org.springframework.ai.chat.client.advisor.api.StreamAroundAdvisorChain;
import org.springframework.ai.chat.metadata.Usage;
import reactor.core.publisher.Flux;

public class CostTrackingAdvisor implements CallAroundAdvisor, StreamAroundAdvisor {

    private static final String ADVISOR_NAME = "CostTrackingAdvisor";
    private static final int ORDER = 1000; // Execute late to capture response stats

    private final MeterRegistry meterRegistry;

    public CostTrackingAdvisor(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
    }

    @Override
    public AdvisedResponse aroundCall(AdvisedRequest advisedRequest, CallAroundAdvisorChain chain) {
        AdvisedResponse response = chain.nextAroundCall(advisedRequest);
        recordUsage(response);
        return response;
    }

    @Override
    public Flux<AdvisedResponse> aroundStream(AdvisedRequest advisedRequest, StreamAroundAdvisorChain chain) {
        // For streaming, tracking tokens is more complex as it depends on the final chunks.
        // This is a simplified placeholder.
        return chain.nextAroundStream(advisedRequest)
                .doOnComplete(() -> {
                    // Record stream completion metrics
                });
    }

    private void recordUsage(AdvisedResponse response) {
        Usage usage = response.response().getMetadata().getUsage();
        if (usage != null) {
            String tenantId = TenantContextHolder.getTenantId();
            if (tenantId == null) tenantId = "anonymous";
            
            meterRegistry.counter("llm.tokens.used", "tenant", tenantId, "type", "prompt")
                    .increment(usage.getPromptTokens());
            meterRegistry.counter("llm.tokens.used", "tenant", tenantId, "type", "generation")
                    .increment(usage.getGenerationTokens());
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
