# MINIKUBE

Minikube is a lightweight solution for Kubernetes that allows you to have a local testing environment without the need for multiple machines. The Minikube solution combines the worker and manager nodes within the same machine, encapsulated in a Docker container. This enables us to have a lightweight and fast Kubernetes cluster, making it ideal for learning the basics of Kubernetes.

## HOW TO INSTALL MINIKUBE

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

## HOW TO START THE CLUSTER

To start the Minikube cluster, use the command minikube start.

Note: Typically, you would start a cluster by initializing it from the manager node and then using the token for adding other nodes. In Minikube, this process is not necessary as it is a single-node solution.    

## INTRODUCTION TO RESOURCE MANAGEMENT IN KUBERNETES

In Kubernetes, there are various types of resources that help manage containerized applications. Let me briefly explain what Pods, Deployments, and Services are:

    Pods:
        Pods are the smallest deployable units in Kubernetes.
        They represent a single instance of a running process in a cluster and can contain one or more containers.
        Containers within a Pod share the same network namespace, allowing them to communicate with each other using localhost.

    Deployments:
        Deployments provide a declarative way to define and manage the desired state of applications.
        They ensure that a specified number of replicas for a Pod are running at all times, making it easy to scale applications up or down.
        Deployments also support rolling updates and rollbacks, allowing for seamless application updates without downtime.

    Services:
        Services enable communication and networking between different sets of Pods.
        They provide a stable endpoint (IP address and DNS name) to access a group of related Pods, regardless of their individual IP addresses.
        There are different types of services, such as ClusterIP, NodePort, and LoadBalancer, each serving specific networking requirements.

In summary, Pods represent the basic building blocks running containers, Deployments manage the deployment and scaling of Pods, and Services enable communication and networking between these Pods, providing a stable way to access them within the Kubernetes cluster.

## OUR DEPLOYMENT AND OUR SERVICE 

Here you can see the deployment file used for our application -> [app-deployments.yaml](./configuration/app-deployments.yaml).

By writing a deployment.yaml file, we can define the creation of Pods and also manage their scalability.

