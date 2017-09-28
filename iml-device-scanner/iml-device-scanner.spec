%define base_name device-scanner
Name:       iml-%{base_name}
Version:    1.1.1
Release:    1%{?dist}
Summary:    Builds an in-memory representation of devices. Uses udev rules to handle change events.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/%{base_name}
Source0:    http://registry.npmjs.org/@iml/%{base_name}/-/%{base_name}-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires: systemd
Requires: nodejs

%description
Builds an in-memory representation of devices. Uses udev rules to handle change events.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_unitdir}
cp %{_builddir}/package/dist/device-scanner-daemon/systemd-units/%{base_name}.socket %{buildroot}%{_unitdir}
cp %{_builddir}/package/dist/device-scanner-daemon/systemd-units/%{base_name}.service %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_libdir}/%{name}-daemon
cp %{_builddir}/package/dist/device-scanner-daemon/device-scanner-daemon %{buildroot}%{_libdir}/%{name}-daemon

mkdir -p %{buildroot}/lib/udev
cp %{_builddir}/package/dist/block-device-listener/block-device-listener %{buildroot}/lib/udev

mkdir -p %{buildroot}/etc/udev/rules.d
cp %{_builddir}/package/dist/block-device-listener/udev-rules/99-iml-device-scanner.rules %{buildroot}/etc/udev/rules.d

%clean
rm -rf %{buildroot}

%files
%dir %{_libdir}/%{name}-daemon
%attr(0755,root,root)%{_libdir}/%{name}-daemon/device-scanner-daemon
%attr(0644,root,root)%{_unitdir}/%{base_name}.service
%attr(0644,root,root)%{_unitdir}/%{base_name}.socket
%attr(0755,root,root)/lib/udev/block-device-listener
%attr(0644,root,root)/etc/udev/rules.d/99-iml-device-scanner.rules

%post
if [ $1 -eq 1 ] ; then
  systemctl enable %{base_name}.socket
  systemctl start %{base_name}.socket
  udevadm trigger --action=change --subsystem-match=block
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
* Wed Sep 27 2017 Joe Grund <joe.grund@intel.com> - 1.1.1-1
- Fix bug where devices weren't removed.
- Cast empty IML_SIZE string to None.

* Thu Sep 21 2017 Joe Grund <joe.grund@intel.com> - 1.1.0-1
- Exclude unneeded devices.
- Get device ro status.
- Remove manual udev parsing.
- Remove socat as dep, device-scanner will listen to change events directly.

* Mon Sep 18 2017 Joe Grund <joe.grund@intel.com> - 1.0.2-1
- Fix missing keys to be option types.
- Add rules for scsi ids
- Add keys on change|add so we can `udevadm trigger` after install
- Trigger udevadm change event after install
- Read new state into scanner after install

* Tue Aug 29 2017 Joe Grund <joe.grund@intel.com> - 1.0.1-1
- initial package