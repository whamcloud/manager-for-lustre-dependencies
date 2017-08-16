# Created by pyp2rpm-3.2.2
%global pypi_name iml-common
%global major_minor 1.0
%global patch 6

Name:           python-%{pypi_name}%{major_minor}
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

%package -n     python2-%{pypi_name}%{major_minor}-%{version}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}%{major_minor}}

%description -n python2-%{pypi_name}%{major_minor}-%{version}
A Python package that contains common components for the IML project Different
areas of the IML project utilise common code that is shared distributed through
this package.This packaging intends to improve code reuse and componentization
within the IML project.


%prep
%autosetup -n %{pypi_name}%{major_minor}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name}%{major_minor}-%{version}
%license license.txt
%doc README.md README.rst
%{python2_sitelib}/iml_common
%{python2_sitelib}/iml_common-%{version}-py?.?.egg-info

%changelog
* Thu Aug 10 2017  - 1.0.6-1
- Initial package.
