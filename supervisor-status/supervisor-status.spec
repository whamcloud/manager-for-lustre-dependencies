%{?nodejs_find_provides_and_requires}

Name:       iml-supervisor-status
Version:    1.0.1
Release:    1%{?dist}
Summary:    Service that reports current supervisor status as JSON.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/supervisor-status
Source0:    http://registry.npmjs.org/@iml/%{name}/-/%{name}-%{version}.tgz
Source1:    iml-supervisor-status.socket
Source2:    iml-supervisor-status.service

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
This module reports supervisord process status as a JSON array as a persistent daemon.
This avoids the need to implement a XMLRPC client everywhere we need status. We can just connect to this socket and get status.
It will either return a top level object with a result key on success, or an error key on failure.
It is meant to be used with unix domain sockets + socket activation.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib/systemd/system/
cp %{SOURCE1} %{buildroot}/usr/lib/systemd/system/%{name}.socket
cp %{SOURCE2} %{buildroot}/usr/lib/systemd/system/%{name}.service
mkdir -p %{buildroot}/usr/lib/%{name}
cp %{_builddir}/package/dist/supervisor-status %{buildroot}/usr/lib/%{name}/supervisor-status

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root)/usr/lib/%{name}/supervisor-status
%attr(0644,root,root)/usr/lib/systemd/system/%{name}.service
%attr(0644,root,root)/usr/lib/systemd/system/%{name}.socket

%post
if [ $1 -eq 1 ] ; then
  systemctl enable %{name}.socket
  systemctl start %{name}.socket
fi

%preun
if [ $1 -eq 0 ] ; then
  systemctl stop %{name}.service
  systemctl disable %{name}.service
  systemctl stop %{name}.socket
  systemctl disable %{name}.socket
  rm /var/run/%{name}.sock
fi

%changelog
* Wed Jul 27 2017 Will Johnson <william.c.johnson@intel.com> - 1.0.1-1
- Put unit files in with dep folder instead of being coupled to the supervisor-status tar file
- Move bundle from /usr/sbin to /usr/lib/iml-supervisor-status

* Wed Jun 14 2017 Joe Grund <joe.grund@intel.com> - 1.0.0-2
- initial package