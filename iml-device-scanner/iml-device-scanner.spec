%define base_name device-scanner
Name:       iml-%{base_name}
Version:    1.0.1
Release:    1%{?dist}
Summary:    Builds an in-memory representation of devices. Uses udev rules to handle change events.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/%{base_name}
Source0:    http://registry.npmjs.org/@iml/%{base_name}/-/%{base_name}-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
Requires: nodejs

%description
Builds an in-memory representation of devices. Uses udev rules to handle change events.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib/systemd/system
cp %{_builddir}/package/dist/device-scanner-daemon/systemd-units/%{base_name}.socket %{buildroot}/usr/lib/systemd/system
cp %{_builddir}/package/dist/device-scanner-daemon/systemd-units/%{base_name}.service %{buildroot}/usr/lib/systemd/system

mkdir -p %{buildroot}/usr/lib/%{name}-daemon
cp %{_builddir}/package/dist/device-scanner-daemon/device-scanner-daemon %{buildroot}/usr/lib/%{name}-daemon

mkdir -p %{buildroot}/lib/udev
cp %{_builddir}/package/dist/block-device-listener/block-device-listener %{buildroot}/lib/udev

mkdir -p %{buildroot}/etc/udev/rules.d
cp %{_builddir}/package/dist/block-device-listener/udev-rules/99-iml-device-scanner.rules %{buildroot}/etc/udev/rules.d

%clean
rm -rf %{buildroot}

%files
%dir /usr/lib/%{name}-daemon
%attr(0755,root,root)/usr/lib/%{name}-daemon/device-scanner-daemon
%attr(0644,root,root)/usr/lib/systemd/system/%{base_name}.service
%attr(0644,root,root)/usr/lib/systemd/system/%{base_name}.socket
%attr(0755,root,root)/lib/udev/block-device-listener
%attr(0644,root,root)/etc/udev/rules.d/99-iml-device-scanner.rules

%post
if [ $1 -eq 1 ] ; then
  systemctl enable %{base_name}.socket
  systemctl start %{base_name}.socket
fi

%preun
if [ $1 -eq 0 ] ; then
  systemctl stop %{base_name}.service
  systemctl disable %{base_name}.service
  systemctl stop %{base_name}.socket
  systemctl disable %{base_name}.socket
  rm /var/run/%{base_name}.sock
fi

%changelog
* Tue Aug 29 2017 Joe Grund <joe.grund@intel.com> - 1.0.1-1
- initial package