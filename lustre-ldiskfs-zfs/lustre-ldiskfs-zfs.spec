Name:		lustre-ldiskfs-zfs
Version:	1
Release:	3%{?dist}
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

%changelog
* Tue Aug 22 2017 Brian J. Murrell <brian.murrell@intel.com> 1-3
- Remove LU-9745 hack now that that is fixed upstream

* Tue Jul 11 2017 Brian J. Murrell <brian.murrell@intel.com> 1-2
- Add %post to work around LU-9745 by removing the autoinstalled
  lustre module and re-installing it

* Fri Jul  7 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
