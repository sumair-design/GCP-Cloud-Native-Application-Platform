# Kubernetes Troubleshooting Lab

Failed pod:

    kubectl get pods -n cloud-native
    kubectl describe pod POD_NAME -n cloud-native
    kubectl logs POD_NAME -n cloud-native

Replacement test:

    kubectl delete pod POD_NAME -n cloud-native
    kubectl get pods -n cloud-native -w

ImagePullBackOff:

    kubectl describe pod POD_NAME -n cloud-native

Check the Artifact Registry hostname, repository, image tag and image existence.

Service discovery:

    kubectl run curl-test --rm -it --image=curlimages/curl -- sh
    curl http://cloud-native-app.cloud-native.svc.cluster.local/

Rolling update:

    helm upgrade cloud-native-app ./helm/cloud-native-app --namespace cloud-native --set image.repository=REGION-docker.pkg.dev/PROJECT_ID/cloud-native-app/web --set image.tag=NEW_TAG
    kubectl rollout status deployment/cloud-native-app-cloud-native-app -n cloud-native

HPA:

    kubectl get hpa -n cloud-native
    kubectl top pods -n cloud-native

Ingress:

    kubectl get ingress -n cloud-native
    kubectl describe ingress cloud-native-app-cloud-native-app -n cloud-native
