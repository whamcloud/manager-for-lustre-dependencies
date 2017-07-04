%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:5]")}

Summary: IML Common
Name: iml-common
Version: 1.0.3
Release: 1%{?dist}
Source0: %{name}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Intel(R) Corporation

%description
Common library containing routines used by both agent and manager.

%package test
Summary: Common test utilities used by Intel Manager for Lustre tests
Group: Development
Requires: %{name} = %{version}-%{release}
%description test
This package contains shared test utilities used in the test framework for Manager for Lustre.

%prep
%setup -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --install-lib=%{python_sitelib} --root=%{buildroot}
mkdir -p $RPM_BUILD_ROOT/usr/sbin/

%clean
rm -rf %{buildroot}

%files
%exclude %{python_sitelib}/iml_common/test
%{python_sitelib}/*

%files test
%{python_sitelib}/iml_common/test
