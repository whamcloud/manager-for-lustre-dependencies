# Created by pyp2rpm-3.2.1
%global pypi_name kombu

Name:           python-%{pypi_name}
Version:        3.0.19
Release:        2%{?dist}
Summary:        Messaging library for Python

License:        TODO
URL:            http://kombu.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools >= 0.7
BuildRequires:  python-nose
BuildRequires:  python2-mock >= 0.7.0
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
BuildRequires:  python-django

%description
.. _kombuindex: kombu Messaging library for Python :Version: 3.0.19Kombu is a
messaging library for Python.The aim of Kombu is to make messaging in Python as
easy as possible by providing an idiomatic highlevel interface for the AMQ
protocol, and also provide proven and tested solutions to common messaging
problems.AMQP_ is the Advanced Message Queuing Protocol, an open standard
protocol for ...

%package -n     python2-%{pypi_name}
Summary:        Messaging library for Python
 
Requires:       python-anyjson >= 0.3.3
Requires:       python-amqp >= 1.4.5
Requires:       python-amqp < 2.0
%description -n python2-%{pypi_name}
.. _kombuindex: kombu Messaging library for Python :Version: 3.0.19Kombu is a
messaging library for Python.The aim of Kombu is to make messaging in Python as
easy as possible by providing an idiomatic highlevel interface for the AMQ
protocol, and also provide proven and tested solutions to common messaging
problems.AMQP_ is the Advanced Message Queuing Protocol, an open standard
protocol for ...

%package -n python-%{pypi_name}-doc
Summary:        kombu documentation
%description -n python-%{pypi_name}-doc
Documentation for kombu

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
# generate html docs 
PYTHONPATH=$PWD sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
%{__python2} setup.py test

%files -n python2-%{pypi_name} 
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Sat May 13 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0.19-2
- Add PYTHONPATH=$PWD to sphinx-build docs html
- Add BuildRequires: python-django

* Sat May 13 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0.19-1
- Initial package.
  * g/python2-setuptools/s//python-setuptools/g
