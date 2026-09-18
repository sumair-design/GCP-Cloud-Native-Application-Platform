# GitHub Actions CI/CD

The workflow validates Python and Helm, authenticates to Google Cloud using Workload Identity Federation, builds an immutable SHA-tagged Docker image, pushes it to Artifact Registry, retrieves GKE credentials, deploys with Helm, and verifies the rollout.

Repository variables:
- GCP_PROJECT_ID
- GKE_CLUSTER
- GKE_LOCATION
- GAR_REGION
- GAR_REPOSITORY

Repository secrets:
- GCP_WORKLOAD_IDENTITY_PROVIDER
- GCP_SERVICE_ACCOUNT

Use a dedicated service account with only the permissions required for Artifact Registry publishing and GKE deployment. Do not store a long-lived JSON key in GitHub.
