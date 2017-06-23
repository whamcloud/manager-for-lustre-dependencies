#!/bin/sh -xe

# This script starts docker and systemd (if el7)

# Version of CentOS/RHEL
el_version=$1

#git log | head -100
export changed_dirs="$(git diff --name-only $TRAVIS_COMMIT_RANGE | sed -ne '/.*\/.*\.spec/s/\/.*//p')"
env > env

 # Run tests in Container
if [ "$el_version" = "6" ]; then
    sudo docker run --rm=true -v $(pwd):/manager-for-lustre-dependencies:rw centos:centos${OS_VERSION} /bin/bash -c "bash -xe /manager-for-lustre-dependencies/test_inside_docker.sh ${OS_VERSION}"
elif [ "$el_version" = "7" ]; then
    docker run --privileged -d -ti -u `id -u $USER` -e "container=docker"  -v /sys/fs/cgroup:/sys/fs/cgroup -v $(pwd):/manager-for-lustre-dependencies:rw  centos:centos${OS_VERSION}   /usr/sbin/init
    DOCKER_CONTAINER_ID=$(docker ps | grep centos | awk '{print $1}')
    docker logs $DOCKER_CONTAINER_ID
    docker exec -ti $DOCKER_CONTAINER_ID /bin/bash -xec "bash -xe /manager-for-lustre-dependencies/test_inside_docker.sh ${OS_VERSION};
      echo -ne \"------\nEND MANAGER-FOR-LUSTRE-DEPENDENCIES TESTS\n\";"
    docker ps -a
    docker stop $DOCKER_CONTAINER_ID
    docker rm -v $DOCKER_CONTAINER_ID
fi
