2. Build and run the container:
```bash
docker-compose up --build
```

3. Check the logs (in another terminal):
```bash
# List volumes
docker volume ls

# Find the volume name (it will be something like docker-volume-demo_app_data)
# Inspect the volume
docker volume inspect docker-volume-demo_app_data

# Check the log file content
docker exec -it docker-volume-demo-app-1 cat /data/app.log
```

4. Stop the container (Ctrl+C in the original terminal)

5. Restart the container:
```bash
docker-compose up
```

Notice that the log file still contains the previous entries because the data persists in the volume.

## Key Concepts

1. **Volume Definition**: In the docker-compose.yml file, we define a named volume `app_data` that will persist data.

2. **Volume Mounting**: The volume is mounted to `/data` in the container, where our application writes its log file.

3. **Data Persistence**: Even if you remove the container, the data in the volume remains:
```bash
# Stop and remove containers
docker-compose down

# Data still exists in volume
docker volume ls
```

4. **Volume Removal**: To remove the volume and its data:
```bash
docker-compose down -v
```

## Testing Data Persistence

1. Run the container and let it write some logs:
```bash
docker-compose up
```

2. Stop the container (Ctrl+C)

3. Remove the container:
```bash
docker-compose down
```

4. Start a new container:
```bash
docker-compose up
```

