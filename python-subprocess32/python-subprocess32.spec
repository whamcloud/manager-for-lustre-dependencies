# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python-subprocess32
Version:        3.2.6
Release:        6%{?dist}
Summary:        Backport of subprocess module from Python 3.2 to Python 2.*

License:        Python
URL:            http://pypi.python.org/pypi/subprocess32/
Source0:        http://python-subprocess32.googlecode.com/files/subprocess32-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-test

%description
Backport of the subprocess module from Python 3.2 for use on 2.x.


%prep
%setup -q -n subprocess32-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%check
PYTHONPATH=$(pwd) %{__python} test_subprocess32.py


%files
%doc LICENSE README.txt
%{python_sitearch}/_posixsubprocess.so
%{python_sitearch}/subprocess32*.egg-info
%{python_sitearch}/subprocess32.py*


%changelog
* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.2.6-6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.6-1
- Update to 3.2.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2.5-0.1.rc1
- Update to new upstream release candidate
- Fix build failure on rawhide

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 David Malcolm <dmalcolm@redhat.com> - 3.2.3-1
- initial package

