Name:		kernel-build-macros
Version:	1
Release:	1%{?dist}
Summary:	RPM macros to build a kernel SRPM

License:	MIT
URL:		https://copr.fedorainfracloud.org/coprs/managerforlustre/

%description
%{summary}

%prep
%autosetup -c -D -T

%build
# Nothing to do

%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
echo '%_with_kabichk 0' > %{buildroot}/%{_rpmconfigdir}/macros.d/macros.kernel-build

%files
%{_rpmconfigdir}/macros.d/macros.kernel-build

%changelog
* Fri Jun 30 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
