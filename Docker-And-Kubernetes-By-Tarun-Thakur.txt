***************************************
***** Docker and Kubernetes Notes *****
***************************************

####################
## Virtualization ##
####################

It is the technique of splitting the physical resource into as many logical resources as we want. In layman's language, it is using one single hardware as multiple isolated hardwares ( using software ). 

Let's consider the case of online coding tutorial. The teacher is sitting at his home and recording the lecture. Many students are watching it. Although each of the student feel that he/she is sitting at the teacher's home attending the lecture, still they share no relation among each other. This is virtualization in everyday life.

############
## Docker ##
############
Docker is a centralized platform-as-a-service for packaging, deploying and running applications.It is written in go language. Before Docker, many developers faced the problem that a particular code runs in the developer's machine but not in the user's machine. A lot of times, the application which you build for your machine doesn't work on other machines because:
-- one or more files are missing
-- software version mistake
-- different configuration

So, the main reason to develop docker is to help developers develop application easily, ship them into containers and deploy them anywhere.

@ Other advantages of docekr:-
-- allows you to use a remote repository to share your container with others
-- provides continuos deployment and testing enviroment 

@ Disadvantages of Docker
-- In docker, it is difficult to manage large number of containers
-- Some features such as container self-registration, container self-inspect etc are missing

++++++++++++++++
++ Containers ++
++++++++++++++++

Docker uses container on the host's operating system to run application.Docker uses OS level virtualization. Container are like system processes that act like an isolated environment. It allows the application to use the host's linux kernel instead of creating a whole virtual operating system. However, it doesn't mean that Docker can not be installed on any other OS. Docker can be installed on Windows and MacOS also. However, it's main component i.e. Docker engine uses linux kernel to run containers.
 Docker automatically bring the dependencies in the container and hence ensures that the app runs anywhere. Containers also allows multiple apps of different version of the same software side by side. So, one app may use node version 14, another may use node version 9. But both the apps may run side by side without disturbing each other.
Another advantage of using a container is that you don't need to allocate any RAM and disk space for the application. It automatically generates the storage and space according to the application requirement.Also, if you want to remove an app, you remove it alongwith all the dependencies in one go. Without Docker, our machine gets cluttered with so many libraries and other dependencies and we are reluctant to delete them out of fear of messing everything.

@ Difference between container and a virtual machine.

-- Container is an isolated environment for running apps whereas virtual machine is an abstraction of the machine.
-- With containers, running multiple apps in isolation is cheaper and easy. On the other hand, while running multiple apps on the virtual machine, we have to create a VM for each app. Each VM needs a full blown os. This makes them slow to start and resource intensiive. Since container doesn't need a whole new copy of the OS, it is light-weight)
-- Container integration is fast and cheap. VM integration is slow and costly
   
@ Why docker container is lightweight ?
 
 Docker containers and host are like a joint family. In India, we have a concept of a joint family where we are free to share each other's resources. You need to pick up your kids from school? you can take your brother's car. You need to host some guest? they can be accomodated in your brother's empty room. Similarly, when other family members need your resources (car, room etc), you will support them. There are some inconviniences, but most of the time, life is " light-wieght".
Similarly, Docker containers share the host’s kernel, network stack, and filesystem drivers, and generally don’t run complex services like systemd or CUPS or sshd; they only run the packaged application. Also, multiple containers share most of the part with the underlying image ( explained below ). A VM generally has a virtualized network setup and disk and runs a full-blown operating system, on top of the OS the host is already running. Hence, Docker conatainers are light weight.  


@ Container FileSystem

Docker containers use a layered filesystem. Docker container is created from a readonly template called docker image. Each docker image references a list of read-only layers that represent a filesystem differences. Layers are stacked on top of each other to form the base for a container's root filesystem. The Docker storage driver is responsible for stacking these layers and providing a single unified view.
When we create a new container, we add a new & thin writable layer on top of the underlying stack of layers present in the base docker image. All change made to the running container, such as creating new files, modyfying existing files, modifying existing files or deleting files, are written to this thin writable container.

@ Containers and Layers
The major difference between a container and an image is the top writable layer. All writes to the container that add or modify existing data are stored in this writable layer. When the container is deleted, the writable layer is also deleted. The underlying image remains unchnged.
Because each container has its own thin writable container layer, and all changes are stored in this container layer, this means multiple containers can share access to the same underlying image and yet have their own data state .
The Docker storage driver is responsible for enabling and managing both the image layer and the writable container layer. Two key technologies behind the Docker image and container management are stackable image layers and copy-on-write (CoW).

@ Copy on Write Strategy

Copy-on-write is a similar strategy of sharing and copying, in which the filesystem processes that need access to the same data share the same instances of that data rather than having their own copy. At some point, if any one process wants to modify or write to the data, only then the OS make a copy of the data for that process to use. Only the process that needs to write has access to the data copy. All other processes continue to use the original data.
Docker makes use of copy-on-write technology with both images and containers. This CoW strategy optimizes both the image disk space usage and the performance of containers. Docker's copy-on-write stratagy not only reduces the amount of space consumed by the containers, but also reduces the time required to start a container. At start time, Docker only has to create the thin writable layer for each container.

++++++++++++++++++++++ 
++ Docker Ecosystem ++
++++++++++++++++++++++

Docker ecosystem consist of the following components :

1. Docker Client : This is the client that the user uses to interacts with docker daemon. Docker client uses commands and REST API to communicate with the docker daemon. When a client runs any server command on the docker client terminal, the client terminal sends these docker commands to the docker daemon. It is possible for docker client to communicate with more than one daemon.
2. Docker Daemon or Docker Engine : It builds the image, makes container out of it and run the containers. Docker daemon runs on the host OS. It is responsible for running containers to manage docker services. Docker daemon can communincate with other docker daemon.
3. Docker Hub : It is a registry (like github) where all the docker images are kept and managed. Anybody can make an account (like github) and put the image in a public or private repository 
4. Docker Images : It is a read-only binary template used to build containers
5. Docker Compose : used in running multiple containers

@ Docker Host
Docker host is used to provide an environment to execute and run application. It contains the docker daemon, images, containers, networks and storages.

+++++++++++++++++++++++++
++ Docker Architecture ++
+++++++++++++++++++++++++

Docker architecture has three main components:
-- Docker Client
-- Docker Host
-- Docker Registry


_______________________  _________________________________________  ______________________
|    ________         |  |        _______________                |  |    ____________    |
|    |Client|         |  |        | Docker Host |                |  |    | Registry |    |
|    ~~~~~~~~         |  |        ~~~~~~~~~~~~~~~                |  |    ~~~~~~~~~~~~    |
| //docker commands   |  |  1.     _________________       2.    |  |                    |
|   $ docker build--->|--|------->| Docker Daemon |------------->|--|---->Ubuntu         |
|   $ docker pull---| |  |        ~~~~~~~~~~~~~~~~~              |  |     |              |
|   $ docker run ---| |  |    ____________         __________    |  |_____|______________|          
~~~~~~~~~~~~~~~~~~~~~~~  |    |Containers|         | Images |    |        V
                         |  |~~~~~~~~~~~~~~|     |~~~~~~~~~~~~|  |        | 
                         |  |    Ubuntu <--|---<-|-Ubuntu <---|--|--<--<--|
                         |  ~~~~~~~~~~~~~~~~  4. ~~~~~~~~~~~~~~  |   3.
                         |_______________________________________|
                         
                         
  -- Diagram flow :
      1. Docker client sends the build image command to the docker daemon.
      2. Since the image we are going to build requires to pull an existing base image (this is generally the os on which the app is based), the docker daemon looks for that image in docker registry (DockerHub)
      3. That image is pulled (downloaded) from the registry and saved in Docker host
      4. Using the saved base image, we build our image and runs the container
      
 
 +++++++++++++++++++     
 ++ Docker Volume ++
 +++++++++++++++++++
 
 Volume is just a directory inside our container. You can declare the directory as a volume only while creating a container. You can't create volume from existing container. You can share one volume across any number of containers. 
 Generally, it is a conventional practive to declare only one volume per container, although you can declare multiple.
 Volume will not be included when you update an image.
 You can map the volume in two ways:-
 1. Container <-------> Container
 2. Host <------------> Container                              
 
@ Benifits of volume
-- Decoupling container from storage. Named volumes are not deleted even if the container is deleted. Hence, our data is safe. 
-- Share volume among different containers
-- on deleting the container, volume does not delete.

$$ Sharing volume with another container

   $ docker run -t --name container2 --privileged=true --volume-from container1  
   
   Now, after creating container2 , volume is visible . Whatever you do in one volume , can be seen from other volume
   
   
????? Docker port expose ????
Let's say that we have created an EC2 instance on AWS. This is our host machine on which we are running linux. Now, we create a docker container on it. But how do we access this container over the internet? You might say that hey, we can access it via the IP address. However, docker container doesn't have the IP address of its own. What we need to do is that connect to the EC2 instance via the IP address and connect to the container through it. For that, we have logical ports. These are available oon every machine and they work in transport layer. In desktop computer machines, they are open by default. In this case, we can map the port number 80 of the EC2 instance to the port 80 of the container. Now when you make an HTTP request to the port 80 of the host EC2 instance, it automatically goes to the port 80 of the container. Similarly the response from the container goes back to the port 80 of the EC2 instance and goes to the user.


################
## Kubernetes ##
################ 

If you carefully see the logos of both docker and kubernetes, you will see that whereas the logo of docker looks like a ship, that of kubernetes looks like a steering of the ship. That's the easiest way of understanding why we need kubernetes.
Kubernetes is a framework for independent container orchestration and docker deployment ( "orchestration" means clustering of any number of containers running on diffrent network and "independent container orchestration" means independent of the cloud provider). It is also known as K8s, 8 represents the number of letters between 'k' and 's'.

In older days, applications had monolithic architecture. ??? All the code was stored on a single file ??? and all the components used to run on a single server. Now, if you want to give  more memory to a particular component, that was not possible. Hence, it had issues on scaling. Another problem in monolithic architechture was that all the components were interelated. So, if you change anything in one component, it might affect another component.
These issues were resolved using a microservice architecture. Here all the components are written as an independent service eg. login service, newFeed service, email service etc. These communicate among each other using API gateway.
Now, let's say that we have different servers for these resources. So, we can deploy them on various servers. But again, here we can't use extra resource of one server with another server. Hence, we use containers. Making multiple containers on one server and assigning each container for each service enables us to use the resources dynamically. Here, we may ask that all this is fine but where does the kubernetes comes into action? Kubernetes helps us control and monitor the containers. Kubernetes is not limited to docker containers. It can handle any container. In fact, Docker itself has a product to handle docker contaners named "Docker Swarm", but kubernetes is more popular in the market.    

I hope it is clear that Kubernetes is an open source container management tool which automates the container deployment, container scaling and load balancing
It schedules, runs and manages isolated containers which are on the virtual/physical/cloud machines.
Developed by Google, Kubernetes is also written in golang

@ Problems with scaling up the containers before kubernetes
-- Autoscaling and load balancing waas not possible
-- Containers had to be managed carefully

@ Features of Kubernetes
-- Orchestration
-- Autoscaling : can do both kinds of scaling -vertical(increasing the capacity of an instance) scaling && horizontal scaling (increasing the number of instances). The preferred scaling is horizontal scaling.
-- Auto-healing
-- Load balancing
-- Platform independent (cloud/virtual/physical)
-- Fault tolerance ( Node/ Pod failure) : In case one of the pods fail, it create a new one. 
-- Health Monitoring of Containers
-- Roll back ( going back to the previous version)
-- Batch execution (one time, sequential,parallel

+++++++++++++++++++++++++++++
++ Kubernetes architecture ++
+++++++++++++++++++++++++++++

Kubernetes follows a master-slave (or client-server) architecture


Cluster-----> Node-----> Pod -------> Container -------> application/microservices

Master: to make master on a ec2 instance, you need at least 2 virtual cpu and 4 gb RAM
                                         ________________________
                                         |Master (control plane)| 
_________________________________________|______________________|_________________________________________
|                                                                        __________________              |
|                                                                        | Kube-Scheduler |              |
|                                                                        ~~~~~~~~~~~~|~~~~~              |
|                                                                                    |                   |
|                                                                                    A                   |
|                                                                                    |                   |
|     ____________                                                                   |                   |
|    | Controller |                                                                  |                   |
|    |   Manager  |                                                                  |                   |
|     ~~~~~~|~~~~~                                                                   |                   |
|           |                             ________________                           |                   |
|           |                             | etcd cluster |                           |                   |
|           |                             |______________|                           |                   |
|           |                                     |                                  A                   |
|           |                                     | Key-value                        |                   |
|           |                                     |                                  |                   |
|           |                              _______|______                     action |                   |
|           <-------------------<----------|API - Server|--------->--------------->---                   |
|                                          ~|~~~|~~~~~|~~                                                | |                                           A   A     A                                                  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~|~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
           __________________               |   |     |
           |    KubeCtl     |----->--------->   A     A
           |(admin/dev/user)|                   |     |
           ~~~~~~~~~~~~~~~~~~                   |     |
                                                |     |
                                                |     |
                                                |     |
                                                A     A
                          ________              |     |
                          |worker|              |     |
        __________________|______|______________|_____|____
        |                                       |     |   |
        |                         Node1         A     A   |
        | ____________                          |     |   |
        | | Kube-roxy|------>------------>-------     |   |     
        | ~~~~~~~~~~~~                                |   |
        | __________                                  |   |
        | | Kubelet|--------->------------>----->------   |
        | ~~~~|~~~~~                                      |
        |     |->---------------->-------|                |
        | ____________________           |                |
        | | container-engine |           V                |
        | ~~~|~~|~~~~~~~~~~~~~           |                |
        |    |  |                        |                |
        |    |  |                        V                |
        |    V  V                        |                |
        |    |  |              __________|_____________   |
        |    |  |              |       Pod 1          |   |
        |    |  |              |  ______________      |   |
        |    |  |--->-------->-|->| Container 1|      |   |
        |    |                 |  ~~~~~~~~~~~~~~      |   |
        |    |                 |  _______________     |   |
        |    |------>-------->-|->| Container 2 |     |   |
        |                      |  ~~~~~~~~~~~~~~~     |   |
        |                      ~~~~~~~~~~~~~~~~~~~~~~~~   |
        |                                                 |
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        
        
1. Kube-api-Server:It is the point of contact for the user. It recieves all the requests and pass them forward. Master communicates to the worker nodes using this. This kube-api-server is meant to scale automatically as per load.

2. Control Manager : Controls the state ( actucal state &  desired). Increase/decreases the number of containers for auto-scaling. It makes suer that the actual state of the cluster matches the desired state. There are two possible choices for control manager: a) If k8 is on cloud, then it will be cloud controlled manager    b) if k8 is on non-cloud then it will be kube-controlled-manager.
Components on master that runs controller :
 a) node-controller: for checking the cloud provider to determine if a node has been detected in the cloud after it stops responding.
 b) route-controller: responsible for setting up network, routes on your cloud
 c) service controller: responsible for load balancer on your cloud against services of type load balancer
 d) volume controller: for creating, attaching and maintaining volumes and interacting with the cloud provider to orchestrate volume    

3. etcd cluster: it is a database that tells the contol Manager about the container requirements. It stores the information about all the pods in key-value pair. It keeps the current state and whenever there is a mismatch between current state and desired state, it tells the control manager. It is a 3rd party entity.But it is very crucial for running kubernetes.It is consistent and highly available. It acts as a source of touch for the cluster state.
etcd has the following features:-
  -- fully relicated - The entire state is available on every node in the cluster
  -- Secure - Implements, automatic TLS with optional client certificate authentication
  -- fast- Benchmarked at 10000 writes per second 

4. Kube-scheduler: It takes the action of matching the actual state to desired state upon direction by control manager.
It handles the pod creation and management. It also assigns the node to create and run pods.
A scheduler watches for newly created pods that have no node assigned. for every pod that the scheduler discovers, the scheduler becomes reponsible for finding best node for that pod to run on.
Scheduler gets the information for hardware configuration for hardware configuration from configuration files and schedule the pods on nodes accordingly. 

5. Kubectl: It sends the "manifest" file that contains all the instructions. The Api server reads it and forwards it to control manager. The control manager then directs the kuber-scheduler accordingly.

6. Kubelet: It is the component of the node that communicates with the API server. It uses port 10255. It controls the pods. let's say that we want to create a new container in the pod. Kubelet send the request to the Api-server which check the actual state in etcd cluster and if there is a mismatch between the desired state and the actual state, then asks the control manager to direct the kube-scheduler to create a new container inside the pod.
It also sends success/fail report to master.

7. Kube-proxy: Handles the networking part.It assigns the IP address to the pod. Always remember that container doesn't have its own ip address. IP address is given to the pods   

8. Pod: It is the smallest unit in kubernetes. In kubernetes, we can't start a container without a pod. A pod can contain any number of containers. However, in practice, we only make one container in a pod. The reason for this is that if we create multiple containers in a pod, then those containers will be tightly coupled (shared volume && running on the same node). In such case, if one of the containers fail then all others will fail too. Also, it is important to remember that pod can not be revived after failure. Once failed, that pod is deleted and a new pod is created in its place. Master only communicates with the pod, it doesn't communicate with containers.
  Pod limitations:
    -- No auto-scaling or auto- healing: We knwo that auto-scaling and auto-healing are the features of kubernetes. But they are not enabled by default, in order to enable them, we need to use the high-level kubernetes objects ( mentioned ahead).
    -- Pod crashes


@ Working with Kubernetes
-- we create a manifest (.yml) file
-- apply this to the cluster ( to master) to bring it into desired state
-- one of the nodes is designated as master, all others as nodes
-- Pod runs on node, which is controlled by master.
-- The master is now going to run a set of K8s processes. These processes will ensure smooth functioning of cluster. These processes are collectively called "Control Plane".
-- Can be multi-master for high availability.
-- Master runs control plane to run cluster smoothly


@ High level kubernetes objects

1. Replication set :For  auto-Scaling and auto-healing
2. Deploymeny: For versioning and roll-back
3. Service: static (non ephemeral), IP and Networking
4.: Volume non ephemeral storage

@ Important Command tools

-- kuberctl: for single cloud
-- kubeadm : on premise
-- kubefed: for federated

@ Labels and Selectors

Labels are the mechanism you use to organise kubernetes object. A label is a key:value pair without any predefined meaning that can be attached to the objects.They are a name for a quick reference. They are similar to tags in AWS or git. It can be given to any object.
Label selectors are used for filtering . The kube-api-server currently uses two types of selectors: equality based ( =, !=) and set based (in, notin and exist).

@ Node-Selector

One use case for selecting labels is to constrain the set of nodes onto which a pod can schedule i.e. you can tell a pod to only be able to run a particular nodes.


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++ Kubernetes Networking, Services, NodePort and Volumes ++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Kubernetes networking addresses four concerns:-

-- Containers within a pod use networking to communicate via loopback.
-- Cluster networking provides cummunication between different pods.
-- The service resources lets you expose an application running in pods to be rechable from outside your cluster.
-- You can also use services to publish services only for consumption inside your cluster.
-- container to container communication on the same pod happens through localhost within the containers.




  


