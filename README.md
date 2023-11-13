# Architettura di Kubernetes

L'architettura di Kubernetes è progettata per orchestrare e gestire container su un cluster di macchine. Ecco un'analisi dettagliata dell'architettura di Kubernetes:

## 1. Cluster Kubernetes

- Il cluster Kubernetes è l'infrastruttura complessiva composta da un set di nodi che eseguono i servizi Kubernetes.
- Un cluster Kubernetes è composto da almeno un nodo master e uno o più nodi worker.

## 2. Nodo Master

- Il nodo master è responsabile della gestione e del controllo globale del cluster.
- Componenti principali sul nodo master:
  - **API Server:** Fornisce l'interfaccia RESTful per interagire con il cluster.
  - **Scheduler:** Assegna i task (pods) ai nodi in base alle risorse disponibili e ai vincoli definiti.
  - **Controller Manager:** Gestisce i controller che regolano lo stato desiderato del sistema.
  - **etcd:** Archivia lo stato del cluster in un datastore distribuito altamente affidabile.

## 3. Nodi Worker

- I nodi worker eseguono i container e forniscono le risorse computazionali e di rete necessarie.
- Componenti principali su ogni nodo worker:
  - **Kubelet:** Agisce come agente su ogni nodo, garantendo che i container siano in uno stato di esecuzione.
  - **Kube-proxy:** Gestisce la rete del cluster, inoltrando il traffico di rete ai container corretti.
  - **Container Runtime:** Il software responsabile dell'esecuzione dei container (es. Docker, containerd).

## 4. Pods

- Il pod è la più piccola unità deployabile in Kubernetes.
- Un pod può contenere uno o più container condividendo lo stesso namespace di rete e lo stesso storage.
- I container all'interno di un pod possono comunicare tra loro attraverso localhost.

## 5. Controller

- I controller in Kubernetes mantengono il numero desiderato di repliche di un'applicazione in esecuzione.
- Tipi comuni di controller includono il ReplicaSet e il Deployment.

## 6. Servizi

- I servizi forniscono un modo persistente per esporre l'applicazione, indipendentemente dal numero di repliche dei pod sottostanti.
- Tipi di servizi includono ClusterIP, NodePort e LoadBalancer.

## 7. ConfigMap e Secrets

- ConfigMap e Secrets sono risorse in Kubernetes utilizzate per gestire configurazioni e dati sensibili rispettivamente.

## 8. Namespace

- I namespace consentono di creare partizioni virtuali all'interno di un cluster Kubernetes.
- Consentono di isolare risorse, utenti e applicazioni all'interno dello stesso cluster.

## 9. Storage

- Kubernetes supporta il provisioning e la gestione di volumi di storage per i container.
- PersistentVolume (PV) e PersistentVolumeClaim (PVC) sono risorse utilizzate per gestire la persistenza dei dati.

## 10. Addon e Custom Resources

- Kubernetes supporta addon come Dashboard, DNS, e ingress controller per estendere la funzionalità del cluster.
- È possibile definire risorse personalizzate (Custom Resource Definitions - CRD) per estendere il modello di oggetti Kubernetes.

In generale, Kubernetes fornisce un'architettura flessibile e modulare che consente la gestione distribuita di applicazioni containerizzate, semplificando la scalabilità, la gestione delle risorse e la distribuzione delle applicazioni in ambienti di produzione.

