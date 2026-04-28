package com.regula.agent.event;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

@Component
public class KafkaAgentTaskPublisher {

    private final KafkaTemplate<String, String> kafkaTemplate;

    public KafkaAgentTaskPublisher(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void publishTaskUpdate(String taskId, String status, String details) {
        // In a real application, you would publish a structured Avro/JSON record
        String payload = String.format("{\"taskId\":\"%s\", \"status\":\"%s\", \"details\":\"%s\"}", taskId, status, details);
        kafkaTemplate.send("agent.task.updates", taskId, payload);
    }
}
