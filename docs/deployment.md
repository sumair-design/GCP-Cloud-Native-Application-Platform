# Deployment

Install the application with Helm:

    helm upgrade --install cloud-native-app ./helm/cloud-native-app --namespace cloud-native --create-namespace --set image.repository=REGION-docker.pkg.dev/PROJECT_ID/cloud-native-app/web --set image.tag=latest

Verify:

    kubectl get deploy,pods,svc,ingress,hpa -n cloud-native
    kubectl rollout status deployment/cloud-native-app-cloud-native-app -n cloud-native

GKE Ingress provisions an external HTTP load balancer. Initial provisioning can take several minutes.
