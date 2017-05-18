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

echo -en 'travis_fold:start:yum install\\r'
yum -y install git mock rpm-build ed
echo -en 'travis_fold:end:yum install\\r'

# add our repos to the mock configuration
ed <<"EOF" /etc/mock/default.cfg
$i

[copr-be.cloud.fedoraproject.org_results_managerforlustre_manager-for-lustre_epel-7-x86_64_]
name=added from: https://copr-be.cloud.fedoraproject.org/results/managerforlustre/manager-for-lustre/epel-7-x86_64/
baseurl=https://copr-be.cloud.fedoraproject.org/results/managerforlustre/manager-for-lustre/epel-7-x86_64/
enabled=1

[lustre-client]
name=added from: https://build.hpdd.intel.com/job/lustre-master/lastSuccessfulBuild/arch=x86_64,build_type=client,distro=el7,ib_stack=inkernel/artifact/artifacts/
baseurl=https://build.hpdd.intel.com/job/lustre-master/lastSuccessfulBuild/arch=x86_64%2Cbuild_type=client%2Cdistro=el7%2Cib_stack=inkernel/artifact/artifacts/
enabled=1
.
w
q
EOF

cd /manager-for-lustre-dependencies
#cat env
eval $(grep ^TRAVIS_COMMIT_RANGE= env)
eval $(grep ^changed_files= env)
#git log | head -100

git diff --name-only $TRAVIS_COMMIT_RANGE

# pretend python-nose is a changed dir and try to build it
cd python-nose
ls -l
chown $USER *
rpmbuild -bs --define epel\ 1 --define _srcrpmdir\ $PWD --define _sourcedir\ $PWD *.spec
echo -en 'travis_fold:start:mock\\r'
mock *.src.rpm
echo -en 'travis_fold:end:mock\\r'
