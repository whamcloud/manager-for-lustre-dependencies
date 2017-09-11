###############################################################################
###############################################################################
##
##  Copyright (C) 2004-2011 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##
###############################################################################
###############################################################################

Name: fence-agents-vbox
Summary: Fence agent for VirtualBox
Requires: openssh-clients
Requires: fence-agents-common
Version: 4.0.24
Release: 2%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sourceware.org/cluster/wiki/
Source0: https://fedorahosted.org/releases/f/e/fence-agents/fence-agents-%{version}.tar.xz
Patch1: fence-agents-%{version}.patch

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/fence-agents-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: glibc-devel
BuildRequires: gnutls-utils
BuildRequires: libxslt
BuildRequires: pexpect python-pycurl python-suds python-requests openwsman-python
BuildRequires: autoconf automake libtool

%prep
%setup -q -n fence-agents-%{version}
%autopatch -p1

%build
./autogen.sh
%{configure}
CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%description
The fence-agents-vbox package contains a fence agent for VirtualBox dom0 accessed via SSH.

%files
%defattr(-,root,root,-)
%{_sbindir}/fence_vbox
%{_mandir}/man8/fence_vbox.8*

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_libexecdir}/fence_kdump_send
find %{buildroot}%{_sbindir}/ -type f ! -name "fence_vbox" | xargs rm
rm -rf %{buildroot}%{_datadir}/cluster/
rm -rf %{buildroot}%{_defaultdocdir}/fence-agents
rm -rf %{buildroot}%{_datadir}/fence/
find %{buildroot}%{_mandir}/man8/ -type f ! -name "fence_vbox*" | xargs rm

%clean
rm -rf %{buildroot}

%post
ccs_update_schema > /dev/null 2>&1 ||:

%changelog
* Fri Aug 11 2017 Joe Grund <joe.grund@intel.com> - 4.0.24-2
- Extract fence-agents-vbox to standalone rpm