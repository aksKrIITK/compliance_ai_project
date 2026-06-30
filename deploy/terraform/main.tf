terraform {
  required_version = ">= 1.5"
  required_providers {
    google = { source = "hashicorp/google", version = "~> 5.0" }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Cloud Run + Cloud SQL + Redis + Storage + Secrets
resource "google_cloud_run_service" "api" {
  name     = "regula-platform"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/regula-platform"
        resources { limits = { memory = "512Mi", cpu = "1" } }
      }
    }
  }
}
