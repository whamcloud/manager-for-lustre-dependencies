# Created by pyp2rpm-3.2.2
%global pypi_name iml-common
%global major_minor 1.0
%global patch 6
%global rpm_name %{pypi_name}%{major_minor}

Name:           python-%{rpm_name}
Version:        %{major_minor}.%{patch}
Release:        1%{?dist}
Summary:        Common library used by multiple IML components

License:        MIT
URL:            https://pypi.python.org/pypi/iml-common
Source0:        https://github.com/intel-hpdd/iml-common/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
A Python package that contains common components for the IML project Different
areas of the IML project utilise common code that is shared distributed through
this package.This packaging intends to improve code reuse and componentization
within the IML project.

%package -n     python2-%{rpm_name}-%{version}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{rpm_name}}

%description -n python2-%{rpm_name}-%{version}
A Python package that contains common components for the IML project Different
areas of the IML project utilise common code that is shared distributed through
this package.This packaging intends to improve code reuse and componentization
within the IML project.

%prep
%setup -c -n %{rpm_name}-%{version}
# Remove bundled egg-info
rm -rf %{rpm_name}.egg-info
pushd .
cd ..
mv %{rpm_name}-%{version}/%{pypi_name}-%{version} ./%{pypi_name}-%{version}
rmdir %{rpm_name}-%{version}
mv %{pypi_name}-%{version} %{rpm_name}-%{version}
popd

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%files -n python2-%{rpm_name}-%{version}
%defattr(-,root,root,-)
%license license.txt
%doc README.md README.rst
%{python2_sitelib}/iml_common
%{python2_sitelib}/iml_common-%{version}-py?.?.egg-info

%changelog
* Thu Aug 10 2017  - 1.0.6-1
- Initial package.