Name:		lustre-ldiskfs-zfs
Version:	1
Release:	2%{?dist}
Summary:	Meta package to install a Lustre storage server with both ldiskfs and ZFS support

License:	MIT
URL:		https://github.com/intel-hpdd/intel-manager-for-lustre

Requires:	lustre
Requires:	lustre-dkms
Requires:	kmod-lustre-osd-ldiskfs
Requires:	zfs

%description
This is a packge you can install if you want to create a Lustre storage
server capable of creating both ldiskfs and ZFS targets.

%prep

%build

%install

%files

%post
# work around LU-9745
lustre_version="$(dkms status -m lustre | sed -e 's/^.*, \(.*\):.*$/\1/')"
lustre_kernel_version="$(rpm -qa | sed -ne 's/kernel-\([0-9].*._lustre.*\)$/\1/p')"
/etc/kernel/postinst.d/dkms $lustre_kernel_version
if [ ! -f /lib/modules/$lustre_kernel_version/extra/lnet.ko ]; then
    dkms uninstall -m lustre/$lustre_version -k $lustre_kernel_version
fi
dkms install -m lustre/$lustre_version -k $lustre_kernel_version

%changelog
* Tue Jul 11 2017 Brian J. Murrell <brian.murrell@intel.com> 1-2
- Add %post to work around LU-9745 by removing the autoinstalled
  lustre module and re-installing it

* Fri Jul  7 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
