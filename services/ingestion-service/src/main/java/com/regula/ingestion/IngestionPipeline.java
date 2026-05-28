package com.regula.ingestion;
import com.regula.ai.TenantAwareVectorStore;
import org.springframework.ai.document.Document;
import org.springframework.ai.reader.tika.TikaDocumentReader;
import org.springframework.ai.transformer.splitter.TokenTextSplitter;
import org.springframework.stereotype.Service;
import org.springframework.core.io.Resource;
import java.util.List;
@Service
public class IngestionPipeline {
    private final TenantAwareVectorStore vectorStore;
    public IngestionPipeline(TenantAwareVectorStore vectorStore) { this.vectorStore = vectorStore; }
    public void ingest(Resource pdfResource) {
        TikaDocumentReader reader = new TikaDocumentReader(pdfResource);
        List<Document> docs = reader.read();
        TokenTextSplitter splitter = new TokenTextSplitter(2000, 500, 10, 500, true);
        List<Document> chunks = splitter.apply(docs);
        vectorStore.add(chunks);
    }
}
