import docker

client = docker.from_env()
containers = client.containers.list(all=True)

for container in containers:
    container_name = container.name

container_found = False

for container in containers:
    if container.name == container_name:
        container.stop()
        print(f"container : {container.name} Stop")
        container.remove()
        print(f"container : {container.name} Removed")
        container_found = True
        break

if not container_found:
    print("Not Found Container")