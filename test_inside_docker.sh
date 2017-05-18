#!/bin/bash -x #e

OS_VERSION=$1

#pwd
#id
#mount
#df -h
#ls -l /home
#ps axf
#rpm -qa

env

yum -y install git mock rpm-build

cd /manager-for-lustre-dependencies
cat env
eval $(grep ^TRAVIS_COMMIT_RANGE= env)
eval $(grep ^changed_files= env)
#git log | head -100

git diff --name-only $TRAVIS_COMMIT_RANGE
