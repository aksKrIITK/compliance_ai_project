package com.regula.agent;
import org.springframework.ai.tool.Tool;
import org.springframework.stereotype.Component;
@Component
public class ToolRegistry {
    @Tool(description = "Send an email to the company director")
    public String sendEmail(String to, String subject, String body) { return "Email sent"; }
    @Tool(description = "Check compliance filing deadlines")
    public String checkDeadlines(String tenantId) { return "Deadline: 30th September"; }
    public Object[] getToolObjects() { return new Object[]{this}; }
}
