package com.regula.agent.controller;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;

@RestController
@RequestMapping("/api/v1/agent")
public class AgentController {

    private final ChatClient agentChatClient;

    public AgentController(ChatClient agentChatClient) {
        this.agentChatClient = agentChatClient;
    }

    @PostMapping(value = "/run", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> runAgentTask(@RequestBody String prompt) {
        return agentChatClient.prompt()
                .user(prompt)
                .stream()
                .content();
    }
}
