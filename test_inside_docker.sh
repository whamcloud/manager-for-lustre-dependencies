#!/bin/bash -x #e

OS_VERSION=$1

#pwd
#id
#mount
#df -h
#ls -l /home
#ps axf
#rpm -qa
cat /etc/passwd

env

#echo -en 'travis_fold:start:yum\\r'
echo 'travis_fold:start:yum'
yum -y install git mock rpm-build ed sudo
echo 'travis_fold:end:yum'

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

eval $(grep ^TRAVIS_COMMIT_RANGE= /manager-for-lustre-dependencies/env)
eval $(grep ^changed_files= /manager-for-lustre-dependencies/env)

useradd mocker
usermod -a -G mock mocker

echo "travis_fold:start:groups"
cat /etc/group
echo "travis_fold:end:groups"

# pretend python-nose is a changed dir and try to build it
SUBDIR=python-nose
su - mocker <<EOF
set -x
pwd
cd /manager-for-lustre-dependencies/$SUBDIR
env
id
rpmbuild -bs --define epel\ 1 --define _srcrpmdir\ $PWD --define _sourcedir\ $PWD *.spec
echo "travis_fold:start:mock"
mock *.src.rpm
echo "travis_fold:end:mock"
EOF

echo "travis_fold:start:journalctl"
journalctl
echo "travis_fold:end:journalctl"
