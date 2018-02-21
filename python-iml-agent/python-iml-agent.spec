%global pypi_name iml-agent
%{!?name: %global name python-%{pypi_name}}
%{?!version: %global version 4.0.0.0}
%{?!package_release: %global package_release 1}
%{?!python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; import sys; sys.stdout.write(get_python_lib())")}

%{?dist_version: %global source https://github.com/intel-hpdd/iml-agent/archive/%{dist_version}.tar.gz}
%{?dist_version: %global archive_version %{dist_version}}
%{?!dist_version: %global source https://pypi.python.org/packages/source/i/iml-agent/iml-agent-%{version}.tar.gz}
%{?!dist_version: %global archive_version %{version}}

Summary: IML Agent
Name: %{name}
Version: %{version}
Release: %{package_release}%{?dist}
Source0: %{source}
License: Proprietary
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Intel Corporation <hpdd-info@intel.com>
Url: http://lustre.intel.com/
BuildRequires: python-setuptools
Obsoletes: chroma-agent
Provides: chroma-agent
Requires: ntp
Requires: python-argparse
Requires: python-daemon
Requires: python-setuptools
Requires: python-requests >= 2.6.0
Requires: python2-tablib
Requires: yum-utils
Requires: initscripts
Requires: iml_sos_plugin
Requires: python2-iml-common1.3
Requires: systemd-python
Requires: python-tzlocal
Requires: python2-toolz
Requires: iml-device-scanner
%if 0%{?rhel} > 5
Requires: util-linux-ng
%endif
Requires(post): selinux-policy
Requires: dnf
Requires: dnf-command(repoquery)

%description
This is the Intel Manager for Lustre monitoring and adminstration agent

%package management
Summary: Management functionality layer.
Group: System/Utility
Conflicts: sysklogd
Obsoletes: chroma-agent-management
Provides: chroma-agent-management

Requires: %{name} = %{version}-%{release}
Requires: pcs
Requires: libxml2-python
Requires: python-netaddr
Requires: python-ethtool
Requires: python-jinja2
Requires: pcapy
Requires: python-impacket
Requires: system-config-firewall-base
Requires: ed

%if 0%{?rhel} < 7
Obsoletes: pacemaker-iml <= 1.1.12-4.wc1.el6
Obsoletes: pacemaker-iml-cluster-libs <= 1.1.12-4.wc1.el6
Obsoletes: pacemaker-iml-libs <= 1.1.12-4.wc1.el6
Obsoletes: pacemaker-iml-cli <= 1.1.12-4.wc1.el6
Requires: pacemaker-iml = 1.1.12-4.wc2.el6
Requires: fence-agents-iml >= 3.1.5-48.wc1.el6.2
%endif

%if 0%{?rhel} > 6
Requires: fence-agents
Requires: fence-agents-virsh
%endif

%description management
This package layers on management capabilities for Intel Manager for Lustre Agent.

%package devel
Summary: Contains stripped .py files
Group: Development
Requires: %{name} = %{version}-%{release}
%description devel
This package contains the .py files stripped out of the production build.

%prep
%setup -n %{pypi_name}-%{archive_version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --install-lib=%{python_sitelib} --install-scripts=%{_bindir} --root=%{buildroot}
mkdir -p $RPM_BUILD_ROOT/usr/sbin/
mv $RPM_BUILD_ROOT/usr/{,s}bin/fence_chroma
mv $RPM_BUILD_ROOT/usr/{,s}bin/chroma-copytool-monitor
mkdir -p $RPM_BUILD_ROOT/etc/{init,logrotate}.d/
cp chroma-agent-init.sh $RPM_BUILD_ROOT/etc/init.d/chroma-agent
cp lustre-modules-init.sh $RPM_BUILD_ROOT/etc/init.d/lustre-modules
install -m 644 logrotate.cfg $RPM_BUILD_ROOT/etc/logrotate.d/chroma-agent

touch management.files
cat <<EndOfList>>management.files
%{python_sitelib}/chroma_agent/action_plugins/manage_*.py*
%{python_sitelib}/chroma_agent/templates/
/usr/lib/ocf/resource.d/chroma/Target
%{_sbindir}/fence_chroma
%{_sbindir}/chroma-copytool-monitor
EndOfList

touch base.files
for base_file in $(find -L $RPM_BUILD_ROOT -type f -name '*.py'); do
  install_file=${base_file/$RPM_BUILD_ROOT\///}
  for mgmt_pat in $(<management.files); do
    if [[ $install_file == $mgmt_pat ]]; then
      continue 2
    fi
  done
  echo "${install_file%.py*}.py*" >> base.files
done

%clean
rm -rf %{buildroot}

%post
chkconfig lustre-modules on
# disable SELinux -- it prevents both lustre and pacemaker from working
sed -ie 's/^SELINUX=.*$/SELINUX=disabled/' /etc/selinux/config
# the above only disables on the next boot.  set to permissive currently, also
setenforce 0

if [ $1 -eq 1 ]; then
    # new install; create default agent config
    chroma-agent reset_agent_config
elif [ $1 -eq 2 ]; then
    # upgrade; convert any older agent config
    chroma-agent convert_agent_config
fi

%triggerin management -- kernel
# when a kernel is installed, make sure that our kernel is reset back to
# being the preferred boot kernel
MOST_RECENT_KERNEL_VERSION=$(rpm -q kernel --qf "%{INSTALLTIME} %{VERSION}-%{RELEASE}.%{ARCH}\n" | sort -nr | sed -n -e '/_lustre/{s/.* //p;q}')
grubby --set-default=/boot/vmlinuz-$MOST_RECENT_KERNEL_VERSION

%files -f base.files
%defattr(-,root,root)
%attr(0755,root,root)/etc/init.d/chroma-agent
%attr(0755,root,root)/etc/init.d/lustre-modules
%{_bindir}/chroma-agent*
%{python_sitelib}/%(a=%{pypi_name}; echo ${a//-/_})-*.egg-info/*
%attr(0644,root,root)/etc/logrotate.d/chroma-agent

%files -f management.files management
%defattr(-,root,root)

%changelog
* Fri Dec  1 2017 Brian J. Murrell <brian.murrell@intel.com> - 4.0.0.0-1
- Initial module
  * split out from the intel-manager-for-lustre project

