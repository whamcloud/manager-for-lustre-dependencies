SRCRPMDIR       := $(shell rpm --eval %_srcrpmdir)
RPMDIR          := $(shell rpm --eval %_rpmdir)
RPMDIST         := $(shell rpm --eval %dist)
VERSION         := $(shell rpm --qf "%{version}\n" -q \
		     --specfile $(NAME).spec | sort -u | \
		     sed -e 's/.el7.*//g')
VERSION_RELEASE := $(shell rpm --qf "%{version}-%{release}\n" -q --specfile \
                     $(NAME).spec | sort -u | sed -e 's/.el7.*//g')
SRPM            := $(NAME)-$(VERSION_RELEASE).el7.src.rpm
SOURCES         := $(shell spectool -l chroma-agent.spec | sed -e 's/.*\///')
TARGETSRPM      := $(SRCRPMDIR)/$(NAME)-$(VERSION_RELEASE).el7.centos.src.rpm
TARGETRPM       := $(RPMDIR)/$(NAME)-$(VERSION_RELEASE).el7.centos.x86_64.rpm

include ../specfile-deps.mk

include ../copr.mk

all: $(TARGETRPM)

srpm: $(TARGETSRPM)

test: $(TARGETSRPM)
	mock $<

$(TARGETSRPM): $(NAME).spec $(SOURCES)
	rpmbuild -bs --define epel\ 1 --define _sourcedir\ $$PWD $<

$(TARGETRPM): $(NAME).spec
	rpmbuild -bb --define epel\ 1 --define _sourcedir\ $$PWD $<

tito_tag:
	tito tag --no-auto-changelog --keep-version

.PHONY: all srpm test tito_tag
