## Create a GKE cluster

A [cluster](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) consists of at least one **cluster master** machine and multiple worker machines called **nodes**. Nodes are [Compute Engine virtual machine (VM) instances](https://cloud.google.com/compute/docs/instances/) that run the Kubernetes processes necessary to make them part of the cluster.

**Note:** Cluster names must start with a letter and end with an alphanumeric, and cannot be longer than 40 characters.

Run the following command:

- Create a cluster
```
gcloud container clusters create --machine-type=e2-medium --zone=ZONE lab-cluster

```


## Get authentication credentials for the cluster



Authenticate with the cluster:
```
gcloud container clusters get-credentials lab-cluster
```

## Deploy an application to the cluster

You can now deploy a containerized application to the cluster. For this lab, you'll run `hello-app` in your cluster.

GKE uses Kubernetes objects to create and manage your cluster's resources. Kubernetes provides the [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) object for deploying stateless applications like web servers. [Service](https://kubernetes.io/docs/concepts/services-networking/service/) objects define rules and load balancing for accessing your application from the internet.

1. To **create a new Deployment** `hello-server` from the `hello-app` container image, run the following [kubectl create](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create) command:
```
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
```



To **create a Kubernetes Service**, which is a Kubernetes resource that lets you expose your application to external traffic, run the following [kubectl expose](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose) command:

```
kubectl expose deployment hello-server --type=LoadBalancer --port 8080
```

To **inspect** the `hello-server` Service, run [kubectl get](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get):

```
kubectl get service
```

To view the application from your web browser, open a new tab and enter the following address, replacing `[EXTERNAL IP]` with the `EXTERNAL-IP` for `hello-server`.
```
http://[EXTERNAL-IP]:8080
```


## Deleting the cluster

1. To **delete** the cluster, run the following command:
```
gcloud container clusters delete lab-cluster
```