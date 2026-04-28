package com.regula.ai.vector;

import com.regula.security.context.TenantContextHolder;
import org.springframework.ai.document.Document;
import org.springframework.ai.vectorstore.SearchRequest;
import org.springframework.ai.vectorstore.VectorStore;

import java.util.List;
import java.util.Optional;

public class TenantAwareVectorStore implements VectorStore {

    private final VectorStore delegate;

    public TenantAwareVectorStore(VectorStore delegate) {
        this.delegate = delegate;
    }

    @Override
    public void add(List<Document> documents) {
        String tenantId = TenantContextHolder.getTenantId();
        if (tenantId != null) {
            documents.forEach(doc -> doc.getMetadata().put("tenant_id", tenantId));
        }
        delegate.add(documents);
    }

    @Override
    public Optional<Boolean> delete(List<String> idList) {
        // In a real implementation, you'd verify ownership before deleting
        return delegate.delete(idList);
    }

    @Override
    public List<Document> similaritySearch(SearchRequest request) {
        String tenantId = TenantContextHolder.getTenantId();
        if (tenantId != null) {
            // Spring AI filter expressions allow programmatic filtering
            request.withFilterExpression("tenant_id == '" + tenantId + "'");
        }
        return delegate.similaritySearch(request);
    }
}
