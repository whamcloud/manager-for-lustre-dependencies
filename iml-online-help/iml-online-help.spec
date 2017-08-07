%define base_name online-help
Name:       iml-%{base_name}
Version:    2.0.0
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
* Mon Aug 07 2017 Will Johnson <william.c.johnson@intel.com> - 2.0.0-1
- Initial package
