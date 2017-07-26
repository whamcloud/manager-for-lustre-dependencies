%{?nodejs_find_provides_and_requires}

Name:       iml-srcmap-reverse
Version:    3.0.5
Release:    1%{?dist}
Summary:    Service that reverses source map traces.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/srcmap-reverse
Source0:    http://registry.npmjs.org/@iml/%{name}/-/%{name}-%{version}.tgz
Source1:    iml-srcmap-reverse.socket
Source2:    iml-srcmap-reverse.service

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
cp %{SOURCE1} %{buildroot}/usr/lib/systemd/system/%{name}.socket
cp %{SOURCE2} %{buildroot}/usr/lib/systemd/system/%{name}.service
mkdir -p %{buildroot}/usr/lib/%{name}
cp %{_builddir}/package/dist/srcmap-reverse.js %{buildroot}/usr/lib/%{name}/srcmap-reverse

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root)/usr/lib/%{name}/srcmap-reverse
%attr(0644,root,root)/usr/lib/systemd/system/%{name}.socket
%attr(0644,root,root)/usr/lib/systemd/system/%{name}.service

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
* Wed Jul 26 2017 William Johnson <william.c.johnson@intel.com> - 3.0.5-1
- initial package