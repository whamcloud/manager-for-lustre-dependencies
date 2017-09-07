%global pypi_name iml_sos_plugin

Name:           %{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A sosreport plugin for collecting IML data.
License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools_scm

Requires:       sos

%description
A sosreport plugin for collecting IML data.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/%{python2_sitelib}/sos/plugins/
mv %{buildroot}/%{python2_sitelib}/iml_sos_plugin/iml.py* %{buildroot}/%{python2_sitelib}/sos/plugins/

%files
%{_bindir}/iml-diagnostics
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python2_sitelib}/sos/plugins/iml.py*

%changelog
* Thu Sep 7 2017 Joe Grund <joe.grund@intel.com> 1.0.1-1
- Initial Relase
