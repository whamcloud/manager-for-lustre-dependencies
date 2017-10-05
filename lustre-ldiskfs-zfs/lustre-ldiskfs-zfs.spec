Name:		lustre-ldiskfs-zfs4.0.0.0
Version:	4.0.0.0
Release:	1%{?dist}
Summary:	Meta package to install a Lustre storage server with both ldiskfs and ZFS support

License:	MIT
URL:		https://github.com/intel-hpdd/intel-manager-for-lustre

Requires:	lustre
Requires:	kmod-lustre-osd-ldiskfs
Requires:	kmod-lustre-osd-zfs
Requires:	zfs = 0.7.1

%description
This is a packge you can install if you want to create a Lustre storage
server capable of creating both ldiskfs and ZFS targets.

%prep

%build

%install

%files

%changelog
* Tue Aug 22 2017 Brian J. Murrell <brian.murrell@intel.com> 4.0.0.0-1
- Use the patchless server packaging and the ZoL repo
- Pin ZFS to the 0.7.1 release
- Version the package so that we don't move all releases
  past, present and future to the same set of Lustre packages
  every time we make a change here

* Tue Aug 22 2017 Brian J. Murrell <brian.murrell@intel.com> 1-3
- Remove LU-9745 hack now that that is fixed upstream

* Tue Jul 11 2017 Brian J. Murrell <brian.murrell@intel.com> 1-2
- Add %post to work around LU-9745 by removing the autoinstalled
  lustre module and re-installing it

* Fri Jul  7 2017 Brian J. Murrell <brian.murrell@intel.com> 1-1
- Initial package
