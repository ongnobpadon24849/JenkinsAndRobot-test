import docker

client =docker.from_env()

containers = client.containers.list()
for container in containers:
    container.stop()
    print(f"container : {container} Stop")
    container.remove()
    print(f"container : {container} Removerd")

images = client.images.list()

for image in images:
    image_id_to_remove = image.id
    print(f"image : {image.id}")
    client.images.remove(image_id_to_remove, force=True)
    print(f"image : {image.id} Removed")