%{?nodejs_find_provides_and_requires}

Name:       iml-srcmap-reverse
Version:    3.0.5
Release:    1%{?dist}
Summary:    Service that reverses source map traces.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/srcmap-reverse
Source0:    http://registry.npmjs.org/@iml/%{name}/-/%{name}-%{version}.tgz
Source1:    iml-srcmap-reverse.service
Source2:    iml-srcmap-reverse.socket

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
This module will run a http server listening on /var/run/iml-srcmap-reverse.sock. When the server receives
a trace statement, it will parallelize the process of reversing the trace against the GUI source map line 
by line.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib/systemd/system/
cp %{_sourcedir}/iml-srcmap-reverse.socket %{buildroot}/usr/lib/systemd/system/iml-srcmap-reverse.socket
cp %{_sourcedir}/iml-srcmap-reverse.service %{buildroot}/usr/lib/systemd/system/iml-srcmap-reverse.service
mkdir -p %{buildroot}/usr/lib/iml-srcmap-reverse
cp %{_builddir}/package/dist/srcmap-reverse.js %{buildroot}/usr/lib/iml-srcmap-reverse/srcmap-reverse

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root)/usr/lib/iml-srcmap-reverse/srcmap-reverse
%attr(0644,root,root)/usr/lib/systemd/system/iml-srcmap-reverse.service
%attr(0644,root,root)/usr/lib/systemd/system/iml-srcmap-reverse.socket

%post
if [ $1 -eq 1 ] ; then
  systemctl enable iml-srcmap-reverse.socket
  systemctl start iml-srcmap-reverse.socket
fi

%preun
if [ $1 -eq 0 ] ; then
  systemctl stop iml-srcmap-reverse.service
  systemctl disable iml-srcmap-reverse.service
  systemctl stop iml-srcmap-reverse.socket
  systemctl disable iml-srcmap-reverse.socket
  rm /var/run/iml-srcmap-reverse.sock
fi

%changelog
* Wed Jul 26 2017 William Johnson <william.c.johnson@intel.com> - 3.0.5-1
- initial package