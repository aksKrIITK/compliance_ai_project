package com.regula.persistence;
import com.regula.security.TenantContext;
import org.springframework.jdbc.datasource.lookup.AbstractRoutingDataSource;
public class TenantAwareRoutingDataSource extends AbstractRoutingDataSource {
    @Override
    protected Object determineCurrentLookupKey() { return TenantContext.getTenantId(); }
}
