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

yum -y install git mock rpmbuild

cd /manager-for-lustre-dependencies
cat env
eval $(grep ^TRAVIS_COMMIT_RANGE= env)
eval $(grep ^changed_files= env)
#git log | head -100

git diff --name-only $TRAVIS_COMMIT_RANGE

# pretend python-nose is a changed dir and try to build it
cd python-nose
rpmbuild -bs --define epel\ 1 --define _srcrpmdir\ $PWD --define _sourcedir\ $PWD *.spec
mock *.src.rpm
