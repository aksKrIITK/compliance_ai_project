package com.regula.agent;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;
@RestController
@RequestMapping("/api/v1/agent")
public class AgentController {
    private final AgentExecutor executor;
    public AgentController(AgentExecutor executor) { this.executor = executor; }
    @PostMapping(value = "/run", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> runTask(@RequestBody AgentTaskRequest request) {
        return executor.execute(request.taskDescription(), request.taskId());
    }
    record AgentTaskRequest(String taskDescription, String taskId) {}
}
