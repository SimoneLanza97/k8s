# SIMPLE GUIDE TO HOST YOUR PRIVATE REGISTRY

## CREATE THE REGISTRY
To create a private registry we will use docker's image registry , which allows us to have a container containing within it an image registry that will be available only to us, so that we can upload our custom images into it without them being accessible to anyone. 
Use the following command to pull the docker image: 
        
        docker pull registry:latest

And use this command to run it (the command run a container named registry , based on registry image , and forward the guest's port 5000 with the host port 5000):

        docker run -d -p 5000:5000 --name registry registry:latest

Now, if you use the command :

        docker ps 

You will see :

        CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                       NAMES
        2ed10fb78b47   registry:latest   "/entrypoint.sh /etc…"   4 seconds ago   Up 3 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   registry

## PUSH THE IMAGE TO THE REGISTRY CONTAINER 

After writing the Dockerfile, we can execute the build to create our image using the following command:

        docker build -t localhost:5000/your_app:1

We create the image with the tag "localhost:5000" so that we can upload it to our personal registry, which is listening on localhost:5000. Perform the login to the private registry with the command:

        docker login localhost:5000

Finally, push our image to the registry using the command:

        docker push localhost:5000/your_app:1

You can also try to delete your local image and pull it from the registry container using the command:

        docker pull localhost:5000/your_app:1 

## NOTE

This is for a test and develop environment, you need to use SSL certificates to use a private registry in production.

Check the documentation :
-> [Docker Registry documentation](https://www.docker.com/blog/how-to-use-your-own-registry-2/)