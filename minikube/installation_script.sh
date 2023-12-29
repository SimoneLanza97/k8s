#!/bin/bash

# QUESTO SCRIPT È RIVOLTO ALL'INSTALLAZIONE DI MINIKUBE IN AMBIENTE LINUX CON ARCH. X86 
# TRAMITE BINARIO 

# download del pacchetto
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
# installazione del pacchetto
sudo install minikube-linux-amd64 /usr/local/bin/minikube
# creazione dell'alias 
echo "alias kubectl="minikube kubectl --"" >> ~/.bashrc

