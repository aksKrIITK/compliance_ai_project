package com.regula.persistence;
import jakarta.persistence.Column;
import jakarta.persistence.MappedSuperclass;
@MappedSuperclass
public abstract class BaseEntity {
    @Column(name = "tenant_id", nullable = false)
    private String tenantId = com.regula.security.TenantContext.getTenantId();
}
