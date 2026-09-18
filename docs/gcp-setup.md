# GCP and GKE Setup

Set the project:

    gcloud config set project YOUR_PROJECT_ID

Enable APIs:

    gcloud services enable container.googleapis.com artifactregistry.googleapis.com iamcredentials.googleapis.com iam.googleapis.com

Create Artifact Registry:

    gcloud artifacts repositories create cloud-native-app --repository-format=docker --location=YOUR_REGION

Create a small GKE Standard lab cluster:

    gcloud container clusters create cloud-native-cluster --location=YOUR_ZONE --machine-type=e2-standard-2 --num-nodes=2 --release-channel=regular

Get credentials:

    gcloud container clusters get-credentials cloud-native-cluster --zone YOUR_ZONE --project YOUR_PROJECT_ID

Do not commit credentials, service-account JSON keys, or real secrets.
