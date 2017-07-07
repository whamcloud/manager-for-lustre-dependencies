Name:		lustre-ldiskfs-zfs
Version:	1
Release:	1%{?dist}
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
/etc/kernel/postinst.d/dkms 3.10.0-514.21.1.el7_lustre.x86_64
if [ ! -f /lib/modules/3.10.0-514.21.1.el7_lustre.x86_64/extra/lnet.ko ]; then
    dkms uninstall -m lustre/2.10.0_RC1 -k 3.10.0-514.21.1.el7_lustre.x86_64
fi

%changelog
* Fri Jul  7 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
