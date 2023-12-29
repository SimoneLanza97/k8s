# MINIKUBE

Minikube è una soluzione light di k8s , permette di avere un ambiente kubernetes per il test locale senza l'utilizzo di più macchine.
La soluzione minikube racchiude nodo worker e manager nella stessa macchina, un container docker, questo ci permette di avere un cluster k8s leggero e veloce, 
ottimo per imparare le basi di kubernetes.

## COME INSTALLARE MINIKUBE
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

## COME AVVIARE IL CLUSTER
Per avviare il cluster minikube, usare il comando "minikube start" 

Nota bene: normalmente dovremmo avviare un cluster partendo dal nodo manager per poi usare il token per l' aggiunta degli altri nodi e una volta completato il processo avremmo il nostro cluster attivo, tutto questo in minikube non serve perchè è una soluzione ad un unico nodo.

## INTERAZIONE CON IL CLUSTER LIVELLO BASE

VISUALIZZARE I NODI PRESENTI NEL CLUSTER 
    kubectl get nodes


