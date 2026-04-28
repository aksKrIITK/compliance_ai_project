package com.regula.compliance.dto;

import lombok.Data;

@Data
public class AskRequest {
    private String question;
    private String conversationId;
}
