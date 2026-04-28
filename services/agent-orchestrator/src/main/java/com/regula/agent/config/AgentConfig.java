package com.regula.agent.config;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AgentConfig {

    @Bean
    public ChatClient agentChatClient(ChatModel chatModel) {
        return ChatClient.builder(chatModel)
                .defaultFunctions("draftPrivacyPolicy", "fileAnnualReport")
                .build();
    }
}
