1. Test Django

```
python manage.py test
```

2. Build Container

```
docker build -f Dockerfile \
    -t registry.digitalocean.com/my-do-private-registry/data-analysis-web:latest \
    -t registry.digitalocean.com/my-do-private-registry/data-analysis-web:v1 \
    .
```

3. Push this container to DO Container Registry

```
docker push registry.digitalocean.com/my-do-private-registry/data-analysis-web --all-tags
```
 
4. Update secrets

```
kubectl delete secret data-analysis-web-prod-env
kubectl create secret generic data-analysis-web-prod-env --from-env-file=src/.prod.env
```

5. Update Deployment

```
kubectl apply -f k8s/app/data-analysis-web.yaml
```

6. Wait for Rollout to finish

```
kubectl rollout status deployment/data-analysis-web-deployment
```

7. Get the Pod name to Migrate it's Database

```
export SINGLE_POD_NAME=$(kubectl get pod -l app=data-analysis-web-deployment -o jsonpath="{.items[0].metadata.name}")
```

or

```
export SINGLE_POD_NAME=$(kubectl get pod -l app=data-analysis-web-deployment -o NAME | tail -n 1
```

8. Run the Migrations on the Pod

```
kubectl exec -it $SINGLE_POD_NAME -- bash /app/migrate.sh
```
