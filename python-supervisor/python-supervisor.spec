# Created by pyp2rpm-3.2.1
%global pypi_name supervisor

Name:           python-%{pypi_name}
Version:        3.0b1
Release:        5%{?dist}
Summary:        A system for controlling process state under UNIX

License:        BSD-derived (http://www.repoze.org/LICENSE.txt)
URL:            http://supervisord.org/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2-mock >= 0.5.0
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

%description
Supervisor Supervisor is a client/server system that allows its users to
control a number of processes on UNIXlike operating systems.Supported Platforms
Supervisor has been tested and is known to run on Linux (Ubuntu), Mac OS X
(10.4, 10.5, 10.6), and Solaris (10 for Intel) and FreeBSD 6.1. It will likely
work fine on most UNIX systems.Supervisor will not run at all under any version
of ...

%package -n     python2-%{pypi_name}
Summary:        A system for controlling process state under UNIX
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-setuptools
Requires:       python-meld3 >= 0.6.5
%description -n python2-%{pypi_name}
Supervisor Supervisor is a client/server system that allows its users to
control a number of processes on UNIXlike operating systems.Supported Platforms
Supervisor has been tested and is known to run on Linux (Ubuntu), Mac OS X
(10.4, 10.5, 10.6), and Solaris (10 for Intel) and FreeBSD 6.1. It will likely
work fine on most UNIX systems.Supervisor will not run at all under any version
of ...

%package -n python-%{pypi_name}-doc
Summary:        supervisor documentation
%description -n python-%{pypi_name}-doc
Documentation for supervisor

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
cp %{buildroot}/%{_bindir}/supervisorctl %{buildroot}/%{_bindir}/supervisorctl-2
ln -sf %{_bindir}/supervisorctl-2 %{buildroot}/%{_bindir}/supervisorctl-%{python2_version}
cp %{buildroot}/%{_bindir}/echo_supervisord_conf %{buildroot}/%{_bindir}/echo_supervisord_conf-2
ln -sf %{_bindir}/echo_supervisord_conf-2 %{buildroot}/%{_bindir}/echo_supervisord_conf-%{python2_version}
cp %{buildroot}/%{_bindir}/supervisord %{buildroot}/%{_bindir}/supervisord-2
ln -sf %{_bindir}/supervisord-2 %{buildroot}/%{_bindir}/supervisord-%{python2_version}
cp %{buildroot}/%{_bindir}/pidproxy %{buildroot}/%{_bindir}/pidproxy-2
ln -sf %{_bindir}/pidproxy-2 %{buildroot}/%{_bindir}/pidproxy-%{python2_version}
# for some reason version.txt does not get installed
cp supervisor/version.txt %{buildroot}/%{python2_sitelib}/%{pypi_name}/


%check
%{__python2} setup.py test

%files -n python2-%{pypi_name} 
%doc README.rst supervisor/medusa/docs/README.html supervisor/medusa/README.txt
%{_bindir}/supervisorctl
%{_bindir}/supervisorctl-2
%{_bindir}/supervisorctl-%{python2_version}
%{_bindir}/echo_supervisord_conf
%{_bindir}/echo_supervisord_conf-2
%{_bindir}/echo_supervisord_conf-%{python2_version}
%{_bindir}/supervisord
%{_bindir}/supervisord-2
%{_bindir}/supervisord-%{python2_version}
%{_bindir}/pidproxy
%{_bindir}/pidproxy-2
%{_bindir}/pidproxy-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/supervisor-3.0b1-py2.7-nspkg.pth
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Mon Jun 26 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0b1-5
- Rename base package to have python- prefix on it as needed by tito

* Mon Jun 26 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0b1-4
- Add python_provide macro to generate proper Provides/Obsoletes tags

* Mon May 15 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0b1-3
- Need to manually copy over version.txt for some reason
  (brian.murrell@intel.com)

* Fri May 12 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0b1-2
- s/python2-setuptools/python-setuptools/g (brian.murrell@intel.com)

* Fri May 12 2017 Brian J. Murrell <brian.murrell@intel.com> 3.0b1-1
- Initial package.
  * change supervisor_3.3.1_py2.7_nspkg.pth to supervisor-3.0b1-py2.7-nspkg.pth
    in %files
