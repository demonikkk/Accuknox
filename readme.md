Wisecow Application on Kubernetes with TLS
This project deploys the Wisecow application on a Kubernetes cluster (Minikube) with secure TLS communication using Ingress.

🚀 How to Run
1. Apply Kubernetes manifests
From the root of the repository:

cd k8s
kubectl apply -f .
This will create the deployment, service, and ingress for the Wisecow application.

2. Generate and apply TLS certificate
Move into the certificate directory and create the TLS secret:

cd certificate

kubectl create secret tls wisecow-tls \
  --cert=tls.crt \
  --key=tls.key \
  -n wisecow
This secret will be used by the ingress controller to enable HTTPS.

3. Expose ingress controller locally
Forward the ingress controller service ports to your machine:

kubectl port-forward svc/ingress-nginx-controller -n ingress-nginx 8080:80 8443:443
4. Access the Wisecow application
Open your browser and visit:

👉 https://localhost:8443/

⚠️ Note: Since the TLS certificate is self-signed, the browser will show a security warning. You can safely proceed, as this is expected for local development.