# GCP Cloud-Native Application Platform

Portfolio project using Google Cloud, GKE, Kubernetes, Docker, Helm, GitHub Actions, Prometheus and Grafana.

Architecture:

    GitHub -> GitHub Actions -> Docker -> Artifact Registry -> GKE
                                                        |
    Internet -> GKE Ingress -> Service -> Pods <-------+
                                      |
                              ConfigMap / Secret
                              Probes / Resources / HPA
                                      |
                                  /metrics
                                      |
                                  Prometheus
                                      |
                                   Grafana

## Capabilities

- Containerized Python web application
- GKE Kubernetes Deployment and rolling updates
- ClusterIP Service and Kubernetes DNS discovery
- GKE Ingress and external load balancing
- ConfigMap and Secret injection
- Readiness and liveness probes
- CPU/memory requests and limits
- Horizontal Pod Autoscaling
- Helm packaging and upgrades
- GitHub Actions CI/CD
- Artifact Registry image publishing
- Workload Identity Federation
- Prometheus application metrics
- Grafana observability
- Troubleshooting labs for failed pods, image pulls, connectivity and scaling

## Endpoints

    /
    /healthz
    /readyz
    /metrics

## Local Docker test

    docker build -f docker/Dockerfile -t cloud-native-app:local .
    docker run --rm -p 8080:8080 cloud-native-app:local

Then open http://localhost:8080/ and http://localhost:8080/metrics.

## Monitoring

Install kube-prometheus-stack as described in monitoring/prometheus/README.md, then deploy the application.

## Security

Only placeholders are stored here. Never commit real secrets or service-account JSON keys. CI/CD uses Workload Identity Federation.

## Cost control

GKE, external load balancing, Artifact Registry and monitoring can incur charges. Use a small lab cluster and delete unused resources.

## Portfolio flow

Code -> Docker -> Artifact Registry -> GKE -> Kubernetes -> Helm -> GitHub Actions -> Prometheus -> Grafana
