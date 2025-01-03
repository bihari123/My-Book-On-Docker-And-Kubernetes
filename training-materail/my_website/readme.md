## extra commands 
```
python -m http.server 8080
docker build -t my_website .

❯ docker images                                                                                             │
│REPOSITORY    TAG       IMAGE ID       CREATED         SIZE                                                 │
│my_website    latest    fa2c4c14a670   7 seconds ago   125MB                                                │
│hello-world   latest    d2c94e258dcb   20 months ago   13.3kB                                               │
│                                                                                                            │
│                                                                                
│❯ docker run -d -p 8080:8080 --name website_container my_website                                            │
│dbd03893503d8a738c9dea862c3fe56ec9206a05126a83fa04ebe8ee0b11b65f   

> docker ps   // all live containers
> docker ps -a // all containers (even the dead ones)
│
│> docker stop <name or container id>
> docker rm <name or container id>

> docker logs website_container     // prev logs
> docker logs website_container -f // running logs
```
