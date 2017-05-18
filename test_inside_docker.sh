#!/bin/bash -xe

OS_VERSION=$1

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

eval $(grep -e "^changed_files=" /manager-for-lustre-dependencies/env)

useradd mocker
usermod -a -G mock mocker

for SUBDIR in $(echo $changed_files | sed -ne '/.*\.spec/s/\/.*\.spec//p'; do
    su - mocker <<EOF
set -xe
cd /manager-for-lustre-dependencies/$SUBDIR
rpmbuild -bs --define epel\ 1 --define _srcrpmdir\ \$PWD --define _sourcedir\ \$PWD *.spec
echo "travis_fold:start:mock"
mock \$PWD/*.src.rpm
echo "travis_fold:end:mock"
EOF
