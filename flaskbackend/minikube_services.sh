#!/bin/bash
minikube start
eval $(minikube -p minikube docker-env)
echo "Building Flask Docker image..."
docker build -t flask-app:latest /path/to/flask-app
echo "Building React Docker image..."
docker build -t react-ui:latest /path/to/react-app
echo "Applying Kubernetes manifests for Flask..."
kubectl apply -f /path/to/flask-deployment.yaml
kubectl apply -f /path/to/flask-service.yaml
echo "Applying Kubernetes manifests for React..."
kubectl apply -f /path/to/react-deployment.yaml
kubectl apply -f /path/to/react-service.yaml
echo "Waiting for Flask pod to be ready..."
kubectl wait --for=condition=ready pod -l app=flask-app --timeout=300s
echo "Waiting for React pod to be ready..."
kubectl wait --for=condition=ready pod -l app=react-ui --timeout=300s
echo "Port forwarding Flask service..."
kubectl port-forward svc/flask-app-service 5000:5000 &
echo "Port forwarding React service..."
kubectl port-forward svc/react-app-service 3000:3000 &
echo "Services are up and running. Flask is available at http://localhost:5000, and React is available at http://localhost:3000"