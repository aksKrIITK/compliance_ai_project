package com.regula.messaging;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;
@Component
public class EventPublisher {
    private final KafkaTemplate<String, Object> kafkaTemplate;
    public EventPublisher(KafkaTemplate<String, Object> kafkaTemplate) { this.kafkaTemplate = kafkaTemplate; }
    public void publish(String topic, Object event) { kafkaTemplate.send(topic, event); }
}
