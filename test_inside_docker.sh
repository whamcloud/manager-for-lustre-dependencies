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

yum -y install git mock

cd /manager-for-lustre-dependencies
git log | head -100

git diff --name-only $TRAVIS_COMMIT_RANGE