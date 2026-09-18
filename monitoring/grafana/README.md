# Grafana

Grafana is installed with kube-prometheus-stack.

Open locally:

    kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring

Find the generated admin password:

    kubectl get secret monitoring-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 --decode

Useful dashboard targets:
- Pod CPU and memory
- Pod restarts
- Deployment replicas
- Application request rate
- Application request latency
- HPA replica count
