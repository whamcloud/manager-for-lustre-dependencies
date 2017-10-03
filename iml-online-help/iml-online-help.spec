%define base_name online-help
Name:       iml-%{base_name}
Version:    2.2.0
Release:    1%{?dist}
Summary:    IML Online Help
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/intel-hpdd/%{base_name}
Source0:    http://registry.npmjs.org/@iml/%{base_name}/-/%{base_name}-%{version}.tgz

BuildArch:  noarch

%description
This module is a static html website based on the online-help markdown docs. The html is generated using jekyll.

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
* Tue Oct 03 2017 Will Johnson <william.c.johnson@intel.com> - 2.2.0-1
- Add contributor docs
- Clean-ups

* Wed Sep 27 2017 Will Johnson <william.c.johnson@intel.com> - 2.1.1-1
- Thorough review of Online Help Docs
- Thorough review of Install Guide
- Thorough review of API docs
- Update root readme file to link to Online Help Docs, Install Guide, and API Docs

* Mon Aug 07 2017 Will Johnson <william.c.johnson@intel.com> - 2.0.3-1
- Initial package
