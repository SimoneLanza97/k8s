# MINIKUBE

Minikube is a lightweight solution for Kubernetes that allows you to have a local testing environment without the need for multiple machines. The Minikube solution combines the worker and manager nodes within the same machine, encapsulated in a Docker container. This enables us to have a lightweight and fast Kubernetes cluster, making it ideal for learning the basics of Kubernetes.

## HOW TO INSTALL MINIKUBE

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

## HOW TO START THE CLUSTER

To start the Minikube cluster, use the command minikube start.

Note: Typically, you would start a cluster by initializing it from the manager node and then using the token for adding other nodes. In Minikube, this process is not necessary as it is a single-node solution.    



