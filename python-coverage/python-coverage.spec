# Created by pyp2rpm-3.2.1
%global pypi_name coverage

Name:           python-%{pypi_name}
Version:        3.5.3
Release:        1%{?dist}
Summary:        Code coverage measurement for Python

License:        BSD
URL:            http://nedbatchelder.com/code/coverage
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch1:	        0001-simplified-trace-function-force-its-use.patch
Patch2:	        0002-show-version-with-newer-patch-level.patch
Patch3:	        0003-Add-ability-to-silence-warnings-on-unimported-source.patch
Patch4:	        0004-Update-patch-version.patch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Coverage.py measures code coverage, typically during test execution. It uses
the code analysis tools and tracing hooks provided in the Python standard
library to determine which lines are executable, and which have been
executed.Coverage.py runs on Pythons 2.3 through 3.3, and PyPy
1.8.Documentation is at nedbatchelder.com < Code repository and issue tracker
are at bitbucket.org < in 3.5: ...

%package -n     python2-%{pypi_name}
Summary:        Code coverage measurement for Python
 
Requires:       python-setuptools
%description -n python2-%{pypi_name}
Coverage.py measures code coverage, typically during test execution. It uses
the code analysis tools and tracing hooks provided in the Python standard
library to determine which lines are executable, and which have been
executed.Coverage.py runs on Pythons 2.3 through 3.3, and PyPy
1.8.Documentation is at nedbatchelder.com < Code repository and issue tracker
are at bitbucket.org < in 3.5: ...


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
# this doesn't get created in 3.5.3
#cp %{buildroot}/%{_bindir}/coverage2 %{buildroot}/%{_bindir}/coverage2-2
#ln -sf %{_bindir}/coverage2-2 %{buildroot}/%{_bindir}/coverage2-%{python2_version}
cp %{buildroot}/%{_bindir}/coverage %{buildroot}/%{_bindir}/coverage-2
ln -sf %{_bindir}/coverage-2 %{buildroot}/%{_bindir}/coverage-%{python2_version}
# this doesn't get created in 3.5.3
#cp %{buildroot}/%{_bindir}/coverage-2.7 %{buildroot}/%{_bindir}/coverage-2.7-2
#ln -sf %{_bindir}/coverage-2.7-2 %{buildroot}/%{_bindir}/coverage-2.7-%{python2_version}


%files -n python2-%{pypi_name} 
%doc README.txt
# this doesn't get created in 3.5.3
#%{_bindir}/coverage2
#%{_bindir}/coverage2-2
#%{_bindir}/coverage2-%{python2_version}
%{_bindir}/coverage
%{_bindir}/coverage-2
%{_bindir}/coverage-%{python2_version}
%{_bindir}/coverage-2.7
#%{_bindir}/coverage-2.7-2
#%{_bindir}/coverage-2.7-%{python2_version}
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}p2-py?.?.egg-info

%changelog
* Mon May 15 2017 Brian J. Murrell <brian.murrell@intel.com> - 3.5.3-1
- Initial package.
  * g/python-setuptools/s//python-setuptools/g
  * comment out some of the %{_bindir}/ creations/packaging
  * add patches:
    o 0001-simplified-trace-function-force-its-use.patch
    o 0002-show-version-with-newer-patch-level.patch
    o 0003-Add-ability-to-silence-warnings-on-unimported-source.patch
    o 0004-Update-patch-version.patch
  * add p2 to %{python2_sitearch}/%{pypi_name}-%{version}p2-py?.?.egg-info
    do accomodate the last patch above
