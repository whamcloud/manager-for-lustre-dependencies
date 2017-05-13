# Created by pyp2rpm-3.2.1
%global pypi_name jsonschema

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        1%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT/X
URL:            http://github.com/Julian/jsonschema
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
 jsonschema jsonschema is an implementation of JSON Schema <>_ for Python
(supporting 2.6+ including Python 3)... codeblock:: python >>> from jsonschema
import validate >>> A sample schema, like what we'd get from json.load() >>>
schema { ... "type" : "object", ... "properties" : { ... "price" : {"type" :
"number"}, ... "name" : {"type" : "string"}, ... }, ... } >>> If no exception
is raised ...

%package -n     python2-%{pypi_name}
Summary:        An implementation of JSON Schema validation for Python

%description -n python2-%{pypi_name}
 jsonschema jsonschema is an implementation of JSON Schema <>_ for Python
(supporting 2.6+ including Python 3)... codeblock:: python >>> from jsonschema
import validate >>> A sample schema, like what we'd get from json.load() >>>
schema { ... "type" : "object", ... "properties" : { ... "price" : {"type" :
"number"}, ... "name" : {"type" : "string"}, ... }, ... } >>> If no exception
is raised ...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files -n python2-%{pypi_name} 
%doc README.rst
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sat May 13 2017 Brian J. Murrell <brian.murrell@intel.com> - 0.8.0-1
- Initial package.
  * g/python2-setuptools/s//python-setuptools/g
  * removed /usr/bin/jsonschema creation and packaging
  * removed packaging %{python2_sitelib}/%{pypi_name}
