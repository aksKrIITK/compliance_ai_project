package com.regula.ai;
import com.regula.security.TenantContext;
import org.springframework.ai.document.Document;
import org.springframework.ai.vectorstore.SearchRequest;
import org.springframework.ai.vectorstore.VectorStore;
import java.util.List;
public class TenantAwareVectorStore implements VectorStore {
    private final VectorStore delegate;
    public TenantAwareVectorStore(VectorStore delegate) { this.delegate = delegate; }
    @Override
    public void add(List<Document> documents) {
        String tenantId = TenantContext.getTenantId();
        documents.forEach(doc -> doc.getMetadata().put("tenant_id", tenantId));
        delegate.add(documents);
    }
    @Override
    public List<Document> similaritySearch(SearchRequest request) {
        String tenantId = TenantContext.getTenantId();
        String filterExpr = request.getFilterExpression() == null ?
                "tenant_id == '" + tenantId + "'" :
                request.getFilterExpression() + " && tenant_id == '" + tenantId + "'";
        return delegate.similaritySearch(
                SearchRequest.from(request).withFilterExpression(filterExpr));
    }
    @Override
    public void delete(List<String> idList) { delegate.delete(idList); }
}
