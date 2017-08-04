Name:       iml-gui
Version:    6.1.0
Release:    1%{?dist}
Summary:    Graphical User Interface for Intel Manager for Lustre.
License:    MIT
Group:      System Environment/Libraries
%define repo_name gui
URL:        https://github.com/intel-hpdd/%{repo_name}
Source0:    http://registry.npmjs.org/@iml/iml-%{repo_name}/-/%{repo_name}-%{version}.tgz

BuildArch:  noarch

%description
This module is a bundled version of the realtime user interface for Intel Manager for Lustre.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p $RPM_BUILD_ROOT/usr/lib/iml-manager/%{name}
cp -a dist/. $RPM_BUILD_ROOT/usr/lib/iml-manager/%{name}/

%clean
rm -rf %{buildroot}

%files 
/usr/lib/iml-manager/%{name}

%changelog
* Fri Aug 04 2017 Will Johnson <william.c.johnson@intel.com> - 6.1.0-1
- Integrate srcmap-reverse

* Wed Jun 14 2017 Joe Grund <joe.grund@intel.com> - 6.0.13-1
- initial package