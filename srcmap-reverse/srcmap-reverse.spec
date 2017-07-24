%{?nodejs_find_provides_and_requires}

Name:       srcmap-reverse
Version:    3.0.3
Release:    1%{?dist}
Summary:    Service that reverses source map traces.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/srcmap-reverse
Source0:    http://registry.npmjs.org/@iml/%{name}/-/%{name}-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
This module will run a http server listening on /var/run/srcmap-reverse.sock. When the server receives
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
cp dist/main.js.map $RPM_BUILD_ROOT/usr/lib/main.js.map

%clean
rm -rf %{buildroot}

%files
%attr(0744,root,root)/usr/sbin/srcmap-reverse
%attr(0444,root,root)/usr/lib/main.js.map
%attr(0744,root,root)/usr/lib/systemd/system/srcmap-reverse.service
%attr(0744,root,root)/usr/lib/systemd/system/srcmap-reverse.socket

%post
if [ $1 -eq 1 ] ; then
  systemctl enable srcmap-reverse.socket
  systemctl start srcmap-reverse.socket
fi

%preun
if [ $1 -eq 0 ] ; then
  systemctl stop srcmap-reverse.service
  systemctl disable srcmap-reverse.service
  systemctl stop srcmap-reverse.socket
  systemctl disable srcmap-reverse.socket
fi

%changelog
* Fri Jul 21 2017 William Johnson <william.c.johnson@intel.com> - 3.0.3
- initial package