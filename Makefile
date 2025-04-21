# Variables
IMAGE_NAME = mira-project
CONTAINER_NAME = mira-container

# Default target
.PHONY: all

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Start the container
start:
	docker run -it --rm --name $(CONTAINER_NAME) \
        -e DISPLAY=$(DISPLAY) \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        --device /dev/snd \
        $(IMAGE_NAME)
# Stop the container
stop:
	docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME)

# Restart the container
restart: stop start

# Show running containers
ps:
	docker ps

# Clean up unused Docker resources
clean:
	docker system prune -f