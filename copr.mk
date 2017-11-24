# local settings to this whole project
-include ../copr-local.mk

# local settings to this package
-include copr-local.mk

# this was for old-style, where we kept the tarball
#copr_rpm: $(TARGETSRPM)
copr_rpm: $(NAME).spec
	ifndef COPR_OWNER
	    $(error COPR_OWNER needs to be set in ../copr-local.mk)
	endif
	ifndef COPR_PROJECT
	    $(error COPR_PROJECT needs to be set in ../copr-local.mk)
	endif
	copr-cli build $(COPR_OWNER)/$(COPR_PROJECT) $<

# this was for old-style, where we kept the tarball
#iml_copr_rpm: $(TARGETSRPM)
iml_copr_rpm: $(NAME).spec
	copr-cli --config ~/.config/copr-mfl build \
	         managerforlustre/manager-for-lustre $<

.PHONY: copr_rpm iml_copr_rpm
