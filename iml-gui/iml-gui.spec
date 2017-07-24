Name:       iml-gui
Version:    6.0.13
Release:    1%{?dist}
Summary:    Graphical User Interface for Intel Manager for Lustre.
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/gui
Source0:    http://registry.npmjs.org/@iml/%{name}/-/%{name}-%{version}.tgz

BuildArch:  noarch

%description
This module is a bundled version of the realtime user interface for Intel Manager for Lustre.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p $RPM_BUILD_ROOT/usr/lib/iml-manager/iml-gui
cp -R dist/ $RPM_BUILD_ROOT/usr/lib/iml-manager/iml-gui

%clean
rm -rf %{buildroot}

%changelog
* Wed Jun 14 2017 Joe Grund <joe.grund@intel.com> - 1.0.0-1
- initial package