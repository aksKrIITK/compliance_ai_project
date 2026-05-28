package com.regula.agent;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;
@Service
public class AgentExecutor {
    private final ChatClient chatClient;
    private final ToolRegistry toolRegistry;
    public AgentExecutor(ChatClient.Builder builder, ToolRegistry toolRegistry) {
        this.toolRegistry = toolRegistry;
        this.chatClient = builder.defaultTools(toolRegistry.getToolObjects()).build();
    }
    public Flux<String> execute(String taskDescription, String taskId) {
        return chatClient.prompt().user(taskDescription).stream().content();
    }
}
