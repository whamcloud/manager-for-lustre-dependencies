%{?nodejs_find_provides_and_requires}

Name:       srcmap-reverse
Version:    3.0.2
Release:    2%{?dist}
Summary:    Service that reports current supervisor status as JSON.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/srcmap-reverse
Source0:    http://registry.npmjs.org/@iml/%{name}/-/%{name}-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
This module will run an http server listening on /var/run/srcmap-reverse.sock. When the server receives
a trace statement, it will parallelize the process of reversing the trace against the GUI source map line 
by line.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp systemd-units/srcmap-reverse.socket $RPM_BUILD_ROOT/usr/lib/systemd/system/srcmap-reverse.socket
cp systemd-units/srcmap-reverse.service $RPM_BUILD_ROOT/usr/lib/systemd/system/srcmap-reverse.service
mkdir -p $RPM_BUILD_ROOT/usr/sbin/
cp dist/srcmap-reverse.js $RPM_BUILD_ROOT/usr/sbin/srcmap-reverse
cp dist/main.js.map $RPM_BUILD_ROOT/usr/sbin/main.js.map

%clean
rm -rf %{buildroot}

%files
%attr(0744,root,root)/usr/sbin/srcmap-reverse
%attr(0744,root,root)/usr/sbin/main.js.map
%attr(0744,root,root)/usr/lib/systemd/system/srcmap-reverse.service
%attr(0744,root,root)/usr/lib/systemd/system/srcmap-reverse.socket

%post
systemctl enable srcmap-reverse.socket
systemctl start srcmap-reverse.socket

%preun
systemctl stop srcmap-reverse.service
systemctl disable srcmap-reverse.service
systemctl stop srcmap-reverse.socket
systemctl disable srcmap-reverse.socket

%changelog
* Fri Jul 21 2017 William Johnson <william.c.johnson@intel.com> - 3.0.2
- initial package