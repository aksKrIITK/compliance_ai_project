package com.regula.compliance;
import com.regula.dto.AskRequest;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;
@RestController
@RequestMapping("/api/v1/compliance")
public class AskController {
    private final ComplianceQAService qaService;
    public AskController(ComplianceQAService qaService) { this.qaService = qaService; }
    @PostMapping(value = "/ask", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> ask(@RequestBody AskRequest request) { return qaService.askStream(request); }
}
