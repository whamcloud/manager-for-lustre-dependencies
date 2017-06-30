Name:		lustre-client-build-macros
Version:	1
Release:	5%{?dist}
Summary:	RPM macros to build a Lustre client SRPM

License:	MIT
URL:		https://copr.fedorainfracloud.org/coprs/managerforlustre/

%description
%{summary}

%prep
%autosetup -c -D -T

%build
# Nothing to do

%install
set -x
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
#echo "%kver 3.10.0-514.26.1.el7.x86_64" > %{buildroot}/%{_rpmconfigdir}/macros.d/macros.lustre-client-build
cat <<EOF > %{buildroot}/%{_rpmconfigdir}/macros.d/macros.lustre-client-build
%%kdir /usr/src/kernels/%%(ls /usr/src/kernels/ | tail -1)
%%_with_servers 0
%%_without_servers 1
EOF

%files
%{_rpmconfigdir}/macros.d/macros.lustre-client-build

%changelog
* Fri Jun 30 2017 Brian J. Murrell <brian.murrell@intel.com> 1-5
- better automatically detect the %%kdir
  - using %%kver requires the kernel RPM to also be installed which
    shouldn't strictly be necessary

* Fri Jun 30 2017 Brian J. Murrell <brian.murrell@intel.com> 1-4
- new package built with tito
- undefine servers macros 
* Fri Jun 30 2017 Brian J. Murrell <brian.murrell@intel.com> 1-3
- don't define as a global

* Fri Jun 30 2017 Brian J. Murrell <brian.murrell@intel.com> 1-2
- double percent in the echo

* Fri Jun 30 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
