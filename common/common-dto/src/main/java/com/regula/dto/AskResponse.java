package com.regula.dto;
import java.util.List;
public record AskResponse(String answer, List<Citation> sources) {
    public record Citation(String text, String sourceDocument, String section) {}
}
