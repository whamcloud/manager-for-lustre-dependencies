%{?nodejs_find_provides_and_requires}

Name:       supervisor-status
Version:    1.0.0
Release:    2%{?dist}
Summary:    Service that reports current supervisor status as JSON.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/supervisor-status
Source0:    http://registry.npmjs.org/@iml/%{name}/-/%{name}-%{version}.tgz

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

mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp systemd-units/supervisor-status.socket $RPM_BUILD_ROOT/usr/lib/systemd/system/supervisor-status.socket
cp systemd-units/supervisor-status.service $RPM_BUILD_ROOT/usr/lib/systemd/system/supervisor-status.service
mkdir -p $RPM_BUILD_ROOT/usr/sbin/
cp dist/supervisor-status $RPM_BUILD_ROOT/usr/sbin/supervisor-status

%clean
rm -rf %{buildroot}

%files
%attr(0744,root,root)/usr/sbin/supervisor-status
%attr(0744,root,root)/usr/lib/systemd/system/supervisor-status.service
%attr(0744,root,root)/usr/lib/systemd/system/supervisor-status.socket

%post
systemctl enable supervisor-status.socket
systemctl start supervisor-status.socket

%preun
systemctl stop supervisor-status.service
systemctl disable supervisor-status.service
systemctl stop supervisor-status.socket
systemctl disable supervisor-status.socket

%changelog
* Wed Jun 14 2017 Joe Grund
- new package built with tito

* Wed Jun 14 2017 Joe Grund <joe.grund@intel.com> - 1.0.0
- initial package