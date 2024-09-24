import docker

client =docker.from_env()

containers = client.containers.list(all=True)

for container in containers:
    container_name = container.name

container_found = False

for container in containers:
    if container.name == container_name:
        container_found = True
        container.stop()
        print(f"container : {container.id} Stop")
        break

if not container_found:
    print("Not Found Container!!!")