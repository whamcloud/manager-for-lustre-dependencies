# we use the upstream version from http_parser.h as the SONAME
%global somajor 2
%global sominor 7
%global sopoint 1

Name:           http-parser
Version:        %{somajor}.%{sominor}.%{sopoint}
Release:        4%{?dist}
Summary:        HTTP request/response parser for C

License:        MIT
URL:            https://github.com/nodejs/http-parser
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/nodejs/http-parser/commit/335850f6b868d3411968cbf5a4d59fe619dee36f
Patch0001:      %{name}-0001-parser-HTTP_STATUS_MAP-XX-and-enum-http_status.patch

BuildRequires:  gcc
BuildRequires:  cmake

%description
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package devel
Summary:        Development headers and libraries for http-parser
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development headers and libraries for http-parser.

%prep
%autosetup -p1
# TODO: try to send upstream?
cat > CMakeLists.txt << EOF
cmake_minimum_required (VERSION 2.8.5)
project (http-parser C)
include (GNUInstallDirs)

set (SRCS http_parser.c)
set (HDRS http_parser.h)
set (TEST_SRCS test.c)

# Non-Strict version
add_library (http_parser \${SRCS})
target_compile_definitions (http_parser
                            PUBLIC -DHTTP_PARSER_STRICT=0)
add_executable (test-nonstrict \${TEST_SRCS})
target_link_libraries (test-nonstrict http_parser)
# Strict version
add_library (http_parser_strict \${SRCS})
target_compile_definitions (http_parser_strict
                            PUBLIC -DHTTP_PARSER_STRICT=1)
add_executable (test-strict \${TEST_SRCS})
target_link_libraries (test-strict http_parser_strict)

set_target_properties (http_parser http_parser_strict
                       PROPERTIES
                           SOVERSION %{somajor}
                           VERSION %{version})

install (TARGETS http_parser http_parser_strict
         LIBRARY DESTINATION \${CMAKE_INSTALL_LIBDIR})
install (FILES \${HDRS}
         DESTINATION \${CMAKE_INSTALL_INCLUDEDIR})

enable_testing ()
add_test (NAME test-nonstrict COMMAND test-nonstrict)
add_test (NAME test-strict COMMAND test-strict)
EOF

%build
mkdir %{_target_platform}
pushd %{_target_platform}
  %cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%check
make test -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libhttp_parser.so.*
%{_libdir}/libhttp_parser_strict.so.*
%doc AUTHORS README.md
%license LICENSE-MIT

%files devel
%{_includedir}/http_parser.h
%{_libdir}/libhttp_parser.so
%{_libdir}/libhttp_parser_strict.so

%changelog
* Mon Nov 21 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.7.1-4
- Use CMake buildsystem

* Tue Oct 25 2016 Nathaniel McCallum <npmccallum@redhat.com> - 2.7.1-3
- Add (upstreamed) status code patch

* Tue Aug 16 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.7.1-2
- Upgrade to version 2.7.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Stephen Gallagher <sgallagh@redhat.com> 2.6.0-1
- Upgrade to version 2.6.0
- Change to new upstream at https://github.com/nodejs/http-parser/

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-8.20121128gitcd01361
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0-3.20121128gitcd01361
- latest git snapshot
- fixes buffer overflow in tests

* Tue Nov 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0-2.20121110git245f6f0
- latest git snapshot
- fixes tests
- use SMP make flags
- build as Release instead of Debug
- ship new strict variant

* Sat Oct 13 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0-1
- new upstream release 2.0
- migrate to GYP buildsystem

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0-1
- New upstream release 1.0
- Remove patches, no longer needed for nodejs
- Fix typo in -devel description
- use github tarball instead of checkout

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6.20100911git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Lubomir Rintel <lkundrak@v3.sk> - 0.3-5.20100911git
- Add support for methods used by node.js

* Thu Nov  4 2010 Dan Hor??k <dan[at]danny.cz> - 0.3-4.20100911git
- build with -fsigned-char

* Wed Sep 29 2010 jkeating - 0.3-3.20100911git
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.3-2.20100911git
- Call ldconfig (Peter Lemenkov)

* Fri Sep 17 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.3-1.20100911git
- Initial packaging

