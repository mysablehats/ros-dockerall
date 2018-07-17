xhost +
DOCKERSH=$(cat openpose_docker.sh)
nvidia-docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -it garyfeng/docker-openpose:latest $DOCKERSH
