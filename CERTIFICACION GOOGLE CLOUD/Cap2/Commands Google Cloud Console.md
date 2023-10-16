![[Pasted image 20231011091418.png]]



![[Pasted image 20231011091432.png]]



### Understanding regions and zones

Certain [Google Compute Engine](https://cloud.google.com/compute/docs/instances "Compute Engine Docs") resources live in regions or zones. A region is a specific geographical location where you can run your resources. Each region has one or more zones. For example, the `us-central1` region denotes a region in the Central United States that has zones `us-central1-a`, `us-central1-b`, `us-central1-c`, and `us-central1-f`. The following table shows zones in their respective regions:

|Western US|Central US|Eastern US|Western Europe|Eastern Asia|
|---|---|---|---|---|
|us-west1-a|us-central1-a|us-east1-b|europe-west1-b|asia-east1-a|
|us-west1-b|us-central1-b|us-east1-c|europe-west1c|asia-east1-b|
|-|us-central1-c|us-east1-d|europe-west1-d|aisia-east1-c|
|-|us-central1-f|-|-|-|

![[Pasted image 20231011091518.png]]![[Pasted image 20231011091549.png]]


![[Pasted image 20231011091657.png]]

In Cloud Shell, run the following `gcloud` command, to view the project id for your project:


![[Pasted image 20231011091746.png]]

gcloud compute project-info describe --project $(gcloud config get-value project)


```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute project-info describe --project $(gcloud config get-value project)
Your active configuration is: [cloudshell-20178]
commonInstanceMetadata:
  fingerprint: duDIfUPUEew=
  items:
  - key: google-compute-default-zone
    value: us-east1-b
  - key: google-compute-default-region
    value: us-east1
  - key: ssh-keys
    value: student-03-c1ec22729b58:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPBl9PlO/E59o6CcXfKwmniGUSAQ8IKs3GXRRdaLrFQyhedPUI7L538l/EbGH6n3YdlI2YhA/yxIhCeBBBEhJ8i/Ysm28GPBL9M4AcdCKxIJPjawEa4zuAkjUrv6bDnQ9IZEOcoKH3Gm0ewKrUkt4RKOutdE7zzJTvtyPatxb42h73FXzhFEXquWsfnTUiO+JcLW/TOV1mJbzJpYX7Rc638k3spyGoqk5LLjjcAnyg1pE50JBv+5uOWK5tsREdYZgDkb6qk6yutZyIWdIW8POcSaDsMcbukOC3Egu+Zt/+OPZQWKcVp1CWrSxXT9NWNYUSnbnjRqJ+GrFKX4INgNML
      student-03-c1ec22729b58@qwiklabs.net
  - key: enable-oslogin
    value: 'true'
  kind: compute#metadata
creationTimestamp: '2023-10-08T07:32:50.892-07:00'
defaultNetworkTier: PREMIUM
defaultServiceAccount: 394500313768-compute@developer.gserviceaccount.com
id: '7939884504553816957'
kind: compute#project
name: qwiklabs-gcp-03-19b6a5b0ddd0
quotas:
- limit: 1000.0
  metric: SNAPSHOTS
  usage: 0.0
- limit: 5.0
  metric: NETWORKS
  usage: 1.0
- limit: 100.0
  metric: FIREWALLS
  usage: 4.0
- limit: 100.0
  metric: IMAGES
  usage: 0.0
- limit: 8.0
  metric: STATIC_ADDRESSES
  usage: 0.0
- limit: 200.0
  metric: ROUTES
  usage: 0.0
- limit: 15.0
  metric: FORWARDING_RULES
  usage: 0.0
- limit: 50.0
  metric: TARGET_POOLS
  usage: 0.0
- limit: 50.0
  metric: HEALTH_CHECKS
  usage: 0.0
- limit: 4.0
  metric: IN_USE_ADDRESSES
  usage: 0.0
- limit: 50.0
  metric: TARGET_INSTANCES
  usage: 0.0
- limit: 10.0
  metric: TARGET_HTTP_PROXIES
  usage: 0.0
- limit: 10.0
  metric: URL_MAPS
  usage: 0.0
- limit: 50.0
  metric: BACKEND_SERVICES
  usage: 0.0
- limit: 100.0
  metric: INSTANCE_TEMPLATES
  usage: 0.0
- limit: 5.0
  metric: TARGET_VPN_GATEWAYS
  usage: 0.0
- limit: 10.0
  metric: VPN_TUNNELS
  usage: 0.0
- limit: 3.0
  metric: BACKEND_BUCKETS
  usage: 0.0
- limit: 10.0
  metric: ROUTERS
  usage: 0.0
- limit: 10.0
  metric: TARGET_SSL_PROXIES
  usage: 0.0
- limit: 10.0
  metric: TARGET_HTTPS_PROXIES
  usage: 0.0
- limit: 10.0
  metric: SSL_CERTIFICATES
  usage: 0.0
- limit: 100.0
  metric: SUBNETWORKS
  usage: 0.0
- limit: 10.0
  metric: TARGET_TCP_PROXIES
  usage: 0.0
- limit: 12.0
  metric: CPUS_ALL_REGIONS
  usage: 0.0
- limit: 0.0
  metric: SECURITY_POLICIES
  usage: 0.0
- limit: 0.0
  metric: SECURITY_POLICY_RULES
  usage: 0.0
- limit: 1000.0
  metric: XPN_SERVICE_PROJECTS
  usage: 0.0
- limit: 20.0
  metric: PACKET_MIRRORINGS
  usage: 0.0
- limit: 100.0
  metric: NETWORK_ENDPOINT_GROUPS
  usage: 0.0
- limit: 6.0
  metric: INTERCONNECTS
  usage: 0.0
- limit: 5000.0
  metric: GLOBAL_INTERNAL_ADDRESSES
  usage: 0.0
- limit: 5.0
  metric: VPN_GATEWAYS
  usage: 0.0
- limit: 100.0
  metric: MACHINE_IMAGES
  usage: 0.0
- limit: 0.0
  metric: SECURITY_POLICY_CEVAL_RULES
  usage: 0.0
- limit: 0.0
  metric: GPUS_ALL_REGIONS
  usage: 0.0
- limit: 5.0
  metric: EXTERNAL_VPN_GATEWAYS
  usage: 0.0
- limit: 1.0
  metric: PUBLIC_ADVERTISED_PREFIXES
  usage: 0.0
- limit: 10.0
  metric: PUBLIC_DELEGATED_PREFIXES
  usage: 0.0
- limit: 128.0
  metric: STATIC_BYOIP_ADDRESSES
  usage: 0.0
- limit: 10.0
  metric: NETWORK_FIREWALL_POLICIES
  usage: 0.0
- limit: 15.0
  metric: INTERNAL_TRAFFIC_DIRECTOR_FORWARDING_RULES
  usage: 0.0
- limit: 15.0
  metric: GLOBAL_EXTERNAL_MANAGED_FORWARDING_RULES
  usage: 0.0
- limit: 50.0
  metric: GLOBAL_INTERNAL_MANAGED_BACKEND_SERVICES
  usage: 0.0
- limit: 50.0
  metric: GLOBAL_EXTERNAL_MANAGED_BACKEND_SERVICES
  usage: 0.0
- limit: 50.0
  metric: GLOBAL_EXTERNAL_PROXY_LB_BACKEND_SERVICES
  usage: 0.0
- limit: 100.0
  metric: GLOBAL_INTERNAL_TRAFFIC_DIRECTOR_BACKEND_SERVICES
  usage: 0.0
selfLink: https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-03-19b6a5b0ddd0
vmDnsSetting: ZONAL_ONLY
xpnProjectStatus: UNSPECIFIED_XPN_PROJECT_STATUS
```
export PROJECT_ID=$(gcloud config get-value project)
export ZONE=$(gcloud config get-value compute/zone)
echo -e "PROJECT ID: $PROJECT_ID\nZONE: $ZONE"

![[Pasted image 20231011091923.png]]
```
gcloud compute instances create gcelab2 --machine-type e2-medium --zone $ZONE
```

```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute instances create gcelab2 --machine-type e2-medium --zone $ZONE

Created [https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-03-19b6a5b0ddd0/zones/us-east1-b/instances/gcelab2].
NAME: gcelab2
ZONE: us-east1-b
MACHINE_TYPE: e2-medium
PREEMPTIBLE: 
INTERNAL_IP: 10.142.0.2
EXTERNAL_IP: 34.74.5.20
STATUS: RUNNING
```





**Command details**

- `gcloud compute` allows you to manage your Compute Engine resources in a format that's simpler than the Compute Engine API.
- `instances create` creates a new instance.
- `gcelab2` is the name of the VM.
- The `--machine-type` flag specifies the machine type as _e2-medium_.
- The `--zone` flag specifies where the VM is created.
- If you omit the `--zone` flag, the `gcloud` tool can infer your desired zone based on your default properties. Other required instance settings, such as `machine type` and `image`, are set to default values if not specified in the `create` command.

```
gcloud compute instances create --help
```

```
gcloud -h
```


More data: 
```
gcloud config --help
```
List the compute instance available in the project: one also can use
```
gcloud compute instances list --filter="name=('gcelab2')"
```

```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute instances list
NAME: gcelab2
ZONE: us-east1-b
MACHINE_TYPE: e2-medium
PREEMPTIBLE: 
INTERNAL_IP: 10.142.0.2
EXTERNAL_IP: 34.74.5.20
STATUS: RUNNING
```
List the firewall rules in the project:
```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute firewall-rules list
NAME: default-allow-icmp
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: icmp
DENY: 
DISABLED: False

NAME: default-allow-internal
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:0-65535,udp:0-65535,icmp
DENY: 
DISABLED: False

NAME: default-allow-rdp
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:3389
DENY: 
DISABLED: False

NAME: default-allow-ssh
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:22
DENY: 
DISABLED: False

To show all fields of the firewall, please show in JSON format: --format=json
To show all fields in table format, please see the examples in --help.

```
List the firewall rules for the default network:

```
gcloud compute firewall-rules list --filter="network='default'"
```




```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute firewall-rules list --filter="network='default'"
NAME: default-allow-icmp
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: icmp
DENY: 
DISABLED: False

NAME: default-allow-internal
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:0-65535,udp:0-65535,icmp
DENY: 
DISABLED: False

NAME: default-allow-rdp
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:3389
DENY: 
DISABLED: False

NAME: default-allow-ssh
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:22
DENY: 
DISABLED: False

To show all fields of the firewall, please show in JSON format: --format=json
To show all fields in table format, please see the examples in --help.
```
List the firewall rules for the default network where the allow rule matches an ICMP rule:
```
gcloud compute firewall-rules list --filter="NETWORK:'default' AND ALLOW:'icmp'"
```



```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute firewall-rules list --filter="NETWORK:'default' AND ALLOW:'icmp'"
NAME: default-allow-icmp
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: icmp
DENY: 
DISABLED: False

NAME: default-allow-internal
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:0-65535,udp:0-65535,icmp
DENY: 
DISABLED: False

To show all fields of the firewall, please show in JSON format: --format=json
To show all fields in table format, please see the examples in --help.
```




# SSH

```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute ssh gcelab2 --zone $ZONE
WARNING: The private SSH key file for gcloud does not exist.
WARNING: The public SSH key file for gcloud does not exist.
WARNING: You do not have an SSH key for gcloud.
WARNING: SSH keygen will be executed to generate a key.
This tool needs to create the directory [/home/student_03_c1ec22729b58/.ssh] before being able to generate SSH keys.

Do you want to continue (Y/n)?  

Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/student_03_c1ec22729b58/.ssh/google_compute_engine
Your public key has been saved in /home/student_03_c1ec22729b58/.ssh/google_compute_engine.pub
The key fingerprint is:
SHA256:nD975WI15Up2RcoXAaZvG4bKy/nzBJN0vhNljbefVNw student_03_c1ec22729b58@cs-587835085794-default
The key's randomart image is:
+---[RSA 3072]----+
|             o...|
|            o  ++|
|           o o.=E|
|       . .. * =.*|
|        S  = B *.|
|        ... = % =|
|         oo  @ =.|
|        . o+= +  |
|         +o+oo   |
+----[SHA256]-----+
Warning: Permanently added 'compute.6095574162662425531' (ECDSA) to the list of known hosts.
Linux gcelab2 5.10.0-26-cloud-amd64 #1 SMP Debian 5.10.197-1 (2023-09-29) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Creating directory '/home/student-03-c1ec22729b58'.
student-03-c1ec22729b58@gcelab2:~$ 
```

```
student_03_c1ec22729b58@cloudshell:~ (qwiklabs-gcp-03-19b6a5b0ddd0)$ gcloud compute firewall-rules list
NAME: default-allow-icmp
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: icmp
DENY: 
DISABLED: False

NAME: default-allow-internal
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:0-65535,udp:0-65535,icmp
DENY: 
DISABLED: False

NAME: default-allow-rdp
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:3389
DENY: 
DISABLED: False

NAME: default-allow-ssh
NETWORK: default
DIRECTION: INGRESS
PRIORITY: 65534
ALLOW: tcp:22
DENY: 
DISABLED: False


```


Add a tag to the virtual machine:
```
gcloud compute instances add-tags gcelab2 --tags http-server,https-server
```


Update the firewall rule to allow:
```
gcloud compute firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server
```

List the firewall rules for the project:
```
gcloud compute firewall-rules list --filter=ALLOW:'80'
```


View the available logs on the system:

```
gcloud logging logs list
```


View the logs that relate to compute resources:
```
gcloud logging logs list --filter="compute"
```

Read the logs related to the resource type of `gce_instance`:

```
gcloud logging read "resource.type=gce_instance" --limit 5
```

Read the logs for a specific virtual machine:

```
gcloud logging read "resource.type=gce_instance AND labels.instance_name='gcelab2'" --limit 5
```