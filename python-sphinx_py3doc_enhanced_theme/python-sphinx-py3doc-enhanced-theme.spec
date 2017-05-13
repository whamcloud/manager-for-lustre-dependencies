# Created by pyp2rpm-3.2.1
%global pypi_name sphinx-py3doc-enhanced-theme

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        1%{?dist}
Summary:        A theme based on the theme of https://docs.python.org/3/ with some responsive enhancements

License:        BSD
URL:            https://github.com/ionelmc/sphinx-py3doc-enhanced-theme
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
 Enhanced Sphinx theme (based on Python 3 docs) .. listtable:: :stubcolumns: 1
* docs |docs| * tests | |travis| * demo default < bare < * package |version|
|downloads|.. |doc .. |travi .. |versio .. |download A theme based on the theme
of with some responsive enhancements.* Free software: BSD licenseInstallation
:: pip install sphinx_py3doc_enhanced_themeAdd this in your documentation's ...

%package -n     python2-%{pypi_name}
Summary:        A theme based on the theme of https://docs.python.org/3/ with some responsive enhancements
 
Requires:       python-setuptools
%description -n python2-%{pypi_name}
 Enhanced Sphinx theme (based on Python 3 docs) .. listtable:: :stubcolumns: 1
* docs |docs| * tests | |travis| * demo default < bare < * package |version|
|downloads|.. |doc .. |travi .. |versio .. |download A theme based on the theme
of with some responsive enhancements.* Free software: BSD licenseInstallation
:: pip install sphinx_py3doc_enhanced_themeAdd this in your documentation's ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files -n python2-%{pypi_name} 
%doc README.rst tests/readme.rst
%{python2_sitelib}/sphinx_py3doc_enhanced_theme
%{python2_sitelib}/sphinx_py3doc_enhanced_theme-%{version}-py?.?.egg-info

%changelog
* Sat May 13 2017 Brian J. Murrell <brian.murrell@intel.com> - 2.4.0-1
- Initial package.
  * built from downloaded tarball, Source0: fixed due to #118
  * g/python2-setuptools/s//python-setuptools/g
  * s/%{pypi_name}/sphinx_py3doc_enhanced_theme/g in %files
