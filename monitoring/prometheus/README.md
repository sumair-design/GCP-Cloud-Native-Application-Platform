# Prometheus

Install kube-prometheus-stack:

    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    helm upgrade --install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace

The application exposes /metrics and the ServiceMonitor discovers it.

Verify:

    kubectl get servicemonitor -n cloud-native
    kubectl get pods -n monitoring
    kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
