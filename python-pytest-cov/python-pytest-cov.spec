# Created by pyp2rpm-3.2.1
%global pypi_name pytest-cov

Name:           python-%{pypi_name}
Version:        2.5.1
Release:        1%{?dist}
Summary:        Pytest plugin for measuring coverage

License:        MIT
URL:            https://github.com/pytest-dev/pytest-cov
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
BuildRequires:  python2-sphinx-py3doc-enhanced-theme
BuildRequires:  python2-sphinxcontrib-napoleon

%description
Overview .. startbadges.. listtable:: :stubcolumns: 1 * docs |docs| * tests |
|travis| |appveyor| |requires| * package | |version| |wheel|
|supportedversions| |supportedimplementations| | |commitssince|.. |doc ..
|travi .. |appveyo .. |require .. |versio .. |commitssinc .. |whee ..
|supportedversion .. |supportedimplementation .. endbadgesThis plugin produces
coverage reports. It supports ...

%package -n     python2-%{pypi_name}
Summary:        Pytest plugin for measuring coverage
 
Requires:       python2-pytest >= 2.6.0
Requires:       python2-coverage >= 3.7.1
Requires:       python-setuptools
%description -n python2-%{pypi_name}
Overview .. startbadges.. listtable:: :stubcolumns: 1 * docs |docs| * tests |
|travis| |appveyor| |requires| * package | |version| |wheel|
|supportedversions| |supportedimplementations| | |commitssince|.. |doc ..
|travi .. |appveyo .. |require .. |versio .. |commitssinc .. |whee ..
|supportedversion .. |supportedimplementation .. endbadgesThis plugin produces
coverage reports. It supports ...

%package -n python-%{pypi_name}-doc
Summary:        pytest-cov documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest-cov

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files -n python2-%{pypi_name} 
%doc docs/readme.rst README.rst
%{python2_sitelib}/pytest_cov.pth
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/pytest_cov-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Sat May 13 2017 Brian J. Murrell <brian.murrell@intel.com> - 2.5.1-1
- Initial package.
  * g/python2-setuptools/s//python-setuptools/g
  * added BuildRequires:  python2-sphinx-py3doc-enhanced-theme
  * added BuildRequires:  python2-sphinxcontrib-napoleon
