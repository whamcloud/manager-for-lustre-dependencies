RPM_SPEC        := $(NAME).spec
VERSION         := $(shell rpm --qf "%{version}\n" -q --specfile \
                     $(RPM_SPEC) | sort -u | sed -e 's/.el7.*//g')
VERSION_RELEASE := $(shell rpm --qf "%{version}-%{release}\n" -q --specfile \
                     $(RPM_SPEC) | sort -u | sed -e 's/.el7.*//g')
RPM_ARCH        := $(shell rpm --qf "%{arch}\n" -q --specfile \
                     $(RPM_SPEC) | head -1)
RPM_DIST        := $(subst .centos,,$(shell rpm --eval %dist))
SRPM            := $(NAME)-$(VERSION_RELEASE)$(RPM_DIST).src.rpm
TARGETSRPM      := _topdir/SRPMS/$(NAME)-$(VERSION_RELEASE)$(RPM_DIST).src.rpm
TARGETRPM       := _topdir/RPMS/$(RPM_ARCH)/$(NAME)-$(VERSION_RELEASE)$(RPM_DIST).$(RPM_ARCH).rpm

PACKAGE_VERSION  := $(VERSION)
ifdef DIST_VERSION
RPM_DIST_VERSION_ARG := --define dist_version\ $(DIST_VERSION)
else
DIST_VERSION	     := $(PACKAGE_VERSION)
endif


SOURCES         := $(shell spectool $(RPM_DIST_VERSION_ARG) \
		     -l $(RPM_SPEC) | sed -e 's/.*\///')

# should always remove the sources if DIST_VERSION was set
ifneq ($(DIST_VERSION),$(PACKAGE_VERSION))
    $(shell rm -f $(SOURCES))
endif

RPMBUILD_ARGS += $(RPM_DIST_VERSION_ARG)                       \
		 --define "_topdir $$PWD/_topdir"              \
		 --define "%dist $(RPM_DIST)"
#		 --define "version $(PACKAGE_VERSION)"         \
#		 --define "package_release $(PACKAGE_RELEASE)" \

all: rpms

include ../specfile-deps.mk

include ../copr.mk

srpm: $(TARGETSRPM)

rpms: $(TARGETRPM)

test: $(TARGETSRPM)
	mock $(RPM_DIST_VERSION_ARG) $<

debug:
	@echo $(SOURCES)

$(TARGETSRPM): $(NAME).spec $(SOURCES)
	rpmbuild -bs $(RPMBUILD_ARGS) --define epel\ 1 --define _sourcedir\ $$PWD $<

$(TARGETRPM): $(NAME).spec $(SOURCES)
	rpmbuild -bb $(RPMBUILD_ARGS) --define epel\ 1 --define _sourcedir\ $$PWD $<

tito_tag:
	tito tag --no-auto-changelog --keep-version

.PHONY: all rpms srpm test tito_tag
