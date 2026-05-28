package com.regula.ai;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.stereotype.Service;
@Service
public class ModelRouterService {
    private final ChatModel cheapModel;
    private final ChatModel expensiveModel;
    public ModelRouterService(ChatModel openAiChatModel, ChatModel bedrockClaudeChatModel) {
        this.cheapModel = openAiChatModel;
        this.expensiveModel = bedrockClaudeChatModel;
    }
    public ChatModel route(String prompt) {
        if (prompt.length() > 200 || prompt.contains("liability")) return expensiveModel;
        return cheapModel;
    }
}
