package com.regula.compliance;
import com.regula.ai.ModelRouterService;
import com.regula.ai.TenantAwareVectorStore;
import com.regula.dto.AskRequest;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.client.advisor.QuestionAnswerAdvisor;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.vectorstore.SearchRequest;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;
@Service
public class ComplianceQAService {
    private final ChatClient chatClient;
    private final TenantAwareVectorStore vectorStore;
    private final ModelRouterService modelRouter;
    public ComplianceQAService(ChatClient.Builder builder, TenantAwareVectorStore vectorStore, ModelRouterService modelRouter) {
        this.vectorStore = vectorStore;
        this.modelRouter = modelRouter;
        this.chatClient = builder
                .defaultAdvisors(new QuestionAnswerAdvisor(vectorStore, SearchRequest.defaults().withTopK(8).withSimilarityThreshold(0.78)))
                .build();
    }
    public Flux<String> askStream(AskRequest request) {
        ChatModel model = modelRouter.route(request.question());
        return chatClient.prompt().user(request.question()).chatModel(model).stream().content();
    }
}
