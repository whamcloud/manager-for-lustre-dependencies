# Created by pyp2rpm-3.2.1
%global pypi_name nose

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        2%{?dist}
Summary:        nose extends unittest to make testing easier

License:        GNU LGPL
URL:            http://readthedocs.org/docs/nose/
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

%description
nose extends the test loading and running features of unittest, making it
easier to write, find and run tests. By default, nose will run tests in files
or directories under the current working directory whose names include "test"
or "Test" at a word boundary (like "test_this" or "functional_test" or
"TestClass" but not "libtest"). Test output is similar to that of unittest, but
also includes ...

%package -n     python2-%{pypi_name}
Summary:        nose extends unittest to make testing easier
 
Requires:       python-setuptools
%description -n python2-%{pypi_name}
nose extends the test loading and running features of unittest, making it
easier to write, find and run tests. By default, nose will run tests in files
or directories under the current working directory whose names include "test"
or "Test" at a word boundary (like "test_this" or "functional_test" or
"TestClass" but not "libtest"). Test output is similar to that of unittest, but
also includes ...

%package -n python-%{pypi_name}-doc
Summary:        nose documentation
%description -n python-%{pypi_name}-doc
Documentation for nose

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
# generate html docs 
sphinx-build doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/nosetests-2.7 %{buildroot}/%{_bindir}/nosetests-2.7-2
ln -sf %{_bindir}/nosetests-2.7-2 %{buildroot}/%{_bindir}/nosetests-2.7-%{python2_version}
cp %{buildroot}/%{_bindir}/nosetests %{buildroot}/%{_bindir}/nosetests-2
ln -sf %{_bindir}/nosetests-2 %{buildroot}/%{_bindir}/nosetests-%{python2_version}
mkdir -p  %{buildroot}/%{_mandir}/man1
mv %{buildroot}/usr/man/man1/* %{buildroot}/%{_mandir}/man1


%check
%{__python2} setup.py test

%files -n python2-%{pypi_name} 
%doc README.txt
%{_bindir}/nosetests-2.7
%{_bindir}/nosetests-2.7-2
%{_bindir}/nosetests-2.7-%{python2_version}
%{_bindir}/nosetests
%{_bindir}/nosetests-2
%{_bindir}/nosetests-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_mandir}

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Fri May 12 2017 Brian J. Murrell <brian.murrell@intel.com> 1.3.0-2
- Move /usr/man/man1/* to and package /usr/man/man1/*

* Fri May 12 2017 Brian J. Murrell <brian.murrell@intel.com> 1.3.0-1
- Initial package using pyp2rpm
  - s/python2-setuptools/python-setuptools/g
