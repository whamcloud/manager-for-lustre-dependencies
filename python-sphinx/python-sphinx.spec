# Created by pyp2rpm-3.2.1
%global pypi_name Sphinx

Name:           %{pypi_name}
Version:        1.6b3
Release:        1%{?dist}
Summary:        Python documentation generator

License:        BSD
URL:            http://sphinx-doc.org/
Source0:        https://files.pythonhosted.org/packages/source/S/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of multiple
reStructuredText sources), written by Georg Brandl. It was originally created
for the new Python documentation, and has excellent facilities for Python
project documentation, but C/C++ is supported as well, and more languages are
Sphinx uses ...

%package -n     python2-%{pypi_name}
Summary:        Python documentation generator
 
Requires:       python-six >= 1.5
Requires:       python2-jinja2 >= 2.3
Requires:       python2-pygments >= 2.0
Requires:       python-docutils >= 0.11
Requires:       python2-snowballstemmer >= 1.1
Conflicts:      python2-babel = 2.0
Requires:       python2-babel >= 1.3
Requires:       python-alabaster < 0.8
Requires:       python-alabaster >= 0.7
Requires:       python2-imagesize
Requires:       python2-requests >= 2.0.0
Requires:       python2-typing
Requires:       python-setuptools
Requires:       python-sphinxcontrib-websupport
%description -n python2-%{pypi_name}
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of multiple
reStructuredText sources), written by Georg Brandl. It was originally created
for the new Python documentation, and has excellent facilities for Python
project documentation, but C/C++ is supported as well, and more languages are
Sphinx uses ...

%package -n python-%{pypi_name}-doc
Summary:        Sphinx documentation
%description -n python-%{pypi_name}-doc
Documentation for Sphinx

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
# generate html docs 
sphinx-build tests/roots/test-setup/doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/sphinx-apidoc %{buildroot}/%{_bindir}/sphinx-apidoc-2
ln -sf %{_bindir}/sphinx-apidoc-2 %{buildroot}/%{_bindir}/sphinx-apidoc-%{python2_version}
cp %{buildroot}/%{_bindir}/sphinx-autogen %{buildroot}/%{_bindir}/sphinx-autogen-2
ln -sf %{_bindir}/sphinx-autogen-2 %{buildroot}/%{_bindir}/sphinx-autogen-%{python2_version}
cp %{buildroot}/%{_bindir}/sphinx-build %{buildroot}/%{_bindir}/sphinx-build-2
ln -sf %{_bindir}/sphinx-build-2 %{buildroot}/%{_bindir}/sphinx-build-%{python2_version}
cp %{buildroot}/%{_bindir}/sphinx-quickstart %{buildroot}/%{_bindir}/sphinx-quickstart-2
ln -sf %{_bindir}/sphinx-quickstart-2 %{buildroot}/%{_bindir}/sphinx-quickstart-%{python2_version}


%files -n python2-%{pypi_name} 
%doc README.rst
%{_bindir}/sphinx-apidoc
%{_bindir}/sphinx-apidoc-2
%{_bindir}/sphinx-apidoc-%{python2_version}
%{_bindir}/sphinx-autogen
%{_bindir}/sphinx-autogen-2
%{_bindir}/sphinx-autogen-%{python2_version}
%{_bindir}/sphinx-build
%{_bindir}/sphinx-build-2
%{_bindir}/sphinx-build-%{python2_version}
%{_bindir}/sphinx-quickstart
%{_bindir}/sphinx-quickstart-2
%{_bindir}/sphinx-quickstart-%{python2_version}
%{python2_sitelib}/sphinx
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Sat May 13 2017 Brian J. Murrell <brian.murrell@intel.com> 1.6b3-1
- Initial package.
  * g/python2-setuptools/s//python-setuptools/g
  * change %files to %{python2_sitearch}/sphinx
  * change %{python2_sitearch} to %{python2_sitelib} in %files
