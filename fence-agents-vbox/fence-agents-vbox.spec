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

# keep around ready for later user
## global alphatag git0a6184070

Name: fence-agents-vbox
Summary: Fence agent for VirtualBox
Requires: openssh-clients
Requires: fence-agents-common
Version: 4.0.24
Release: 1%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sourceware.org/cluster/wiki/
Source0: https://fedorahosted.org/releases/f/e/fence-agents/fence-agents-%{version}.tar.xz

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
## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents
# remove everything else
rm -rf %{buildroot}/usr/libexec/fence_kdump_send
rm -rf %{buildroot}/usr/sbin/fence_ack_manual
rm -rf %{buildroot}/usr/sbin/fence_alom
rm -rf %{buildroot}/usr/sbin/fence_amt
rm -rf %{buildroot}/usr/sbin/fence_amt_ws
rm -rf %{buildroot}/usr/sbin/fence_apc
rm -rf %{buildroot}/usr/sbin/fence_apc_snmp
rm -rf %{buildroot}/usr/sbin/fence_bladecenter
rm -rf %{buildroot}/usr/sbin/fence_brocade
rm -rf %{buildroot}/usr/sbin/fence_cisco_mds
rm -rf %{buildroot}/usr/sbin/fence_cisco_ucs
rm -rf %{buildroot}/usr/sbin/fence_compute
rm -rf %{buildroot}/usr/sbin/fence_docker
rm -rf %{buildroot}/usr/sbin/fence_drac
rm -rf %{buildroot}/usr/sbin/fence_drac5
rm -rf %{buildroot}/usr/sbin/fence_dummy
rm -rf %{buildroot}/usr/sbin/fence_eaton_snmp
rm -rf %{buildroot}/usr/sbin/fence_emerson
rm -rf %{buildroot}/usr/sbin/fence_eps
rm -rf %{buildroot}/usr/sbin/fence_hds_cb
rm -rf %{buildroot}/usr/sbin/fence_hpblade
rm -rf %{buildroot}/usr/sbin/fence_ibmblade
rm -rf %{buildroot}/usr/sbin/fence_idrac
rm -rf %{buildroot}/usr/sbin/fence_ifmib
rm -rf %{buildroot}/usr/sbin/fence_ilo
rm -rf %{buildroot}/usr/sbin/fence_ilo2
rm -rf %{buildroot}/usr/sbin/fence_ilo3
rm -rf %{buildroot}/usr/sbin/fence_ilo3_ssh
rm -rf %{buildroot}/usr/sbin/fence_ilo4
rm -rf %{buildroot}/usr/sbin/fence_ilo4_ssh
rm -rf %{buildroot}/usr/sbin/fence_ilo_moonshot
rm -rf %{buildroot}/usr/sbin/fence_ilo_mp
rm -rf %{buildroot}/usr/sbin/fence_ilo_ssh
rm -rf %{buildroot}/usr/sbin/fence_imm
rm -rf %{buildroot}/usr/sbin/fence_intelmodular
rm -rf %{buildroot}/usr/sbin/fence_ipdu
rm -rf %{buildroot}/usr/sbin/fence_ipmilan
rm -rf %{buildroot}/usr/sbin/fence_kdump
rm -rf %{buildroot}/usr/sbin/fence_ldom
rm -rf %{buildroot}/usr/sbin/fence_lpar
rm -rf %{buildroot}/usr/sbin/fence_mpath
rm -rf %{buildroot}/usr/sbin/fence_netio
rm -rf %{buildroot}/usr/sbin/fence_ovh
rm -rf %{buildroot}/usr/sbin/fence_pve
rm -rf %{buildroot}/usr/sbin/fence_raritan
rm -rf %{buildroot}/usr/sbin/fence_rcd_serial
rm -rf %{buildroot}/usr/sbin/fence_rhevm
rm -rf %{buildroot}/usr/sbin/fence_rsa
rm -rf %{buildroot}/usr/sbin/fence_rsb
rm -rf %{buildroot}/usr/sbin/fence_sanbox2
rm -rf %{buildroot}/usr/sbin/fence_sbd
rm -rf %{buildroot}/usr/sbin/fence_scsi
rm -rf %{buildroot}/usr/sbin/fence_tripplite_snmp
rm -rf %{buildroot}/usr/sbin/fence_virsh
rm -rf %{buildroot}/usr/sbin/fence_vmware
rm -rf %{buildroot}/usr/sbin/fence_vmware_soap
rm -rf %{buildroot}/usr/sbin/fence_wti
rm -rf %{buildroot}/usr/sbin/fence_xenapi
rm -rf %{buildroot}/usr/sbin/fence_zvm
rm -rf %{buildroot}/usr/sbin/fence_zvmip
rm -rf %{buildroot}/usr/share/cluster/fence_scsi_check
rm -rf %{buildroot}/usr/share/cluster/fence_scsi_check_hardreboot
rm -rf %{buildroot}/usr/share/cluster/relaxng/fence.rng.head
rm -rf %{buildroot}/usr/share/cluster/relaxng/fence.rng.tail
rm -rf %{buildroot}/usr/share/cluster/relaxng/fence2man.xsl
rm -rf %{buildroot}/usr/share/cluster/relaxng/fence2rng.xsl
rm -rf %{buildroot}/usr/share/cluster/relaxng/fence2wiki.xsl
rm -rf %{buildroot}/usr/share/cluster/relaxng/metadata.rng
rm -rf %{buildroot}/usr/share/fence/XenAPI.py
rm -rf %{buildroot}/usr/share/fence/XenAPI.pyc
rm -rf %{buildroot}/usr/share/fence/XenAPI.pyo
rm -rf %{buildroot}/usr/share/fence/fencing.py
rm -rf %{buildroot}/usr/share/fence/fencing.pyc
rm -rf %{buildroot}/usr/share/fence/fencing.pyo
rm -rf %{buildroot}/usr/share/fence/fencing_snmp.py
rm -rf %{buildroot}/usr/share/fence/fencing_snmp.pyc
rm -rf %{buildroot}/usr/share/fence/fencing_snmp.pyo
rm -rf %{buildroot}/usr/share/man/man8/fence_ack_manual.8
rm -rf %{buildroot}/usr/share/man/man8/fence_alom.8
rm -rf %{buildroot}/usr/share/man/man8/fence_amt.8
rm -rf %{buildroot}/usr/share/man/man8/fence_amt_ws.8
rm -rf %{buildroot}/usr/share/man/man8/fence_apc.8
rm -rf %{buildroot}/usr/share/man/man8/fence_apc_snmp.8
rm -rf %{buildroot}/usr/share/man/man8/fence_bladecenter.8
rm -rf %{buildroot}/usr/share/man/man8/fence_brocade.8
rm -rf %{buildroot}/usr/share/man/man8/fence_cisco_mds.8
rm -rf %{buildroot}/usr/share/man/man8/fence_cisco_ucs.8
rm -rf %{buildroot}/usr/share/man/man8/fence_compute.8
rm -rf %{buildroot}/usr/share/man/man8/fence_docker.8
rm -rf %{buildroot}/usr/share/man/man8/fence_drac.8
rm -rf %{buildroot}/usr/share/man/man8/fence_drac5.8
rm -rf %{buildroot}/usr/share/man/man8/fence_dummy.8
rm -rf %{buildroot}/usr/share/man/man8/fence_eaton_snmp.8
rm -rf %{buildroot}/usr/share/man/man8/fence_emerson.8
rm -rf %{buildroot}/usr/share/man/man8/fence_eps.8
rm -rf %{buildroot}/usr/share/man/man8/fence_hds_cb.8
rm -rf %{buildroot}/usr/share/man/man8/fence_hpblade.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ibmblade.8
rm -rf %{buildroot}/usr/share/man/man8/fence_idrac.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ifmib.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo2.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo3.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo3_ssh.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo4.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo4_ssh.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo_moonshot.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo_mp.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ilo_ssh.8
rm -rf %{buildroot}/usr/share/man/man8/fence_imm.8
rm -rf %{buildroot}/usr/share/man/man8/fence_intelmodular.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ipdu.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ipmilan.8
rm -rf %{buildroot}/usr/share/man/man8/fence_kdump.8
rm -rf %{buildroot}/usr/share/man/man8/fence_kdump_send.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ldom.8
rm -rf %{buildroot}/usr/share/man/man8/fence_lpar.8
rm -rf %{buildroot}/usr/share/man/man8/fence_mpath.8
rm -rf %{buildroot}/usr/share/man/man8/fence_netio.8
rm -rf %{buildroot}/usr/share/man/man8/fence_ovh.8
rm -rf %{buildroot}/usr/share/man/man8/fence_pve.8
rm -rf %{buildroot}/usr/share/man/man8/fence_raritan.8
rm -rf %{buildroot}/usr/share/man/man8/fence_rcd_serial.8
rm -rf %{buildroot}/usr/share/man/man8/fence_rhevm.8
rm -rf %{buildroot}/usr/share/man/man8/fence_rsa.8
rm -rf %{buildroot}/usr/share/man/man8/fence_rsb.8
rm -rf %{buildroot}/usr/share/man/man8/fence_sanbox2.8
rm -rf %{buildroot}/usr/share/man/man8/fence_sbd.8
rm -rf %{buildroot}/usr/share/man/man8/fence_scsi.8
rm -rf %{buildroot}/usr/share/man/man8/fence_tripplite_snmp.8
rm -rf %{buildroot}/usr/share/man/man8/fence_virsh.8
rm -rf %{buildroot}/usr/share/man/man8/fence_vmware.8
rm -rf %{buildroot}/usr/share/man/man8/fence_vmware_soap.8
rm -rf %{buildroot}/usr/share/man/man8/fence_wti.8
rm -rf %{buildroot}/usr/share/man/man8/fence_xenapi.8
rm -rf %{buildroot}/usr/share/man/man8/fence_zvm.8
rm -rf %{buildroot}/usr/share/man/man8/fence_zvmip.8

%clean
rm -rf %{buildroot}

%post
ccs_update_schema > /dev/null 2>&1 ||:

%changelog
* Fri Aug 26 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.24-1
- new upstream release

* Wed Jul 13 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.23-2
- fix build issue on s390

* Tue Jul 12 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.23-1
- new upstream release
- new package fence-agents-amt-ws
- new package fence-agents-compute
- new package fence-agents-drac
- new package fence-agents-hds-cb
- new package fence-agents-mpath
- new package fence-agents-sanbox2
- new package fence-agents-sbd
- new package fence-agents-vbox
- new package fence-agents-vmware
- new package fence-agents-xenapi

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Marek Grac <mgrac@redhat.com> - 4.0.20-1
- new upstream release
- new package fence-agents-rcd-serial

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 Marek Grac <mgrac@redhat.com> - 4.0.16-1
- new upstream release

* Mon Feb 09 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-1
- new upstream release

* Thu Jan 08 2015 Marek Grac <mgrac@redhat.com> - 4.0.14-1
- new upstream release
- new packages fence-agents-zvm and fence-agents-emerson

* Thu Oct 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.12-1
- new upstream release
- new package fence-agents-ilo-ssh

* Wed Aug 27 2014 Marek Grac <mgrac@redhat.com> - 4.0.10
- new upstream release
- new package fence-agents-ilo-moonshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.9
- new upstream release
- new package fence-agents-pve

* Mon Apr 07 2014 Marek Grac <mgrac@redhat.com> - 4.0.8-1
- new upstream release
- new package fence-agents-raritan

* Wed Feb 26 2014 Marek Grac <mgrac@redhat.com> - 4.0.7-3
- requires a specific version of fence-agents-common

* Mon Feb 17 2014 Marek Grac <mgrac@redhat.com> - 4.0.7-2
- new upstream release
- changed dependancy from nss/nspr to gnutls-utils

* Fri Jan 10 2014 Marek Grac <mgrac@redhat.com> - 4.0.4-4
- new upstream release
- new package fence-agents-amt

* Mon Oct 07 2013 Marek Grac <mgrac@redhat.com> - 4.0.4-3
- new upstream release
- new package fence-agents-netio

* Tue Sep 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.3-1
- new upstream release
- new packages fence-agents-brocade and fence-agents-ovh

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 4.0.1-2
- Perl 5.18 rebuild

* Mon Jul 01 2013 Marek Grac <mgrac@redhat.com> - 4.0.1-1
- new upstream release

* Mon Jun 24 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-5
- fence-agents-all should provide fence-agent for clean update path

* Wed Apr 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-4
- minor changes in spec file

* Thu Mar 21 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-3
- minor changes in spec file

* Mon Mar 18 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-2
- minor changes in spec file

* Mon Mar 11 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-1
- new upstream release
- introducing subpackages


