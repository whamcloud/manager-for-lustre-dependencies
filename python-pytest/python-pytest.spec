# Created by pyp2rpm-3.2.1
%global pypi_name pytest

Name:           python-%{pypi_name}
Version:        3.0.7
Release:        1%{?dist}
Summary:        pytest: simple powerful testing with Python

License:        MIT license
URL:            http://pytest.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

%description
 The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.An example of a
simple test:.. codeblock:: python content of test_sample.py def inc(x): return
x + 1 def test_answer(): assert inc(3) 5 To execute it:: $ pytest test session
starts collected 1 items test_sample.py F FAILURES
_________________________________ ...

%package -n     python2-%{pypi_name}
Summary:        pytest: simple powerful testing with Python
 
Requires:       python2-py >= 1.4.29
Requires:       python-setuptools
%description -n python2-%{pypi_name}
 The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.An example of a
simple test:.. codeblock:: python content of test_sample.py def inc(x): return
x + 1 def test_answer(): assert inc(3) 5 To execute it:: $ pytest test session
starts collected 1 items test_sample.py F FAILURES
_________________________________ ...

%package -n python-%{pypi_name}-doc
Summary:        pytest documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
# generate html docs 
PYTHONPATH=$PWD sphinx-build doc/en html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/pytest %{buildroot}/%{_bindir}/pytest-2
ln -sf %{_bindir}/pytest-2 %{buildroot}/%{_bindir}/pytest-%{python2_version}
cp %{buildroot}/%{_bindir}/py.test %{buildroot}/%{_bindir}/py.test-2
ln -sf %{_bindir}/py.test-2 %{buildroot}/%{_bindir}/py.test-%{python2_version}


%files -n python2-%{pypi_name} 
%doc README.rst _pytest/vendored_packages/README.md
%{_bindir}/pytest
%{_bindir}/pytest-2
%{_bindir}/pytest-%{python2_version}
%{_bindir}/py.test
%{_bindir}/py.test-2
%{_bindir}/py.test-%{python2_version}

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/_pytest
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Fri May 12 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0.7-1
- Initial package.
  * g/python2-setuptools/s//python-setuptools/g
  * set PYTHONPATH=$PWD for sphinx-build
