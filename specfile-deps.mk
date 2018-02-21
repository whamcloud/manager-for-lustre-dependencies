# generate and include dependencies from the specfile Source*:s
$(shell spectool $(RPM_DIST_VERSION_ARG) -l $(RPM_SPEC) | \
	    sed -e 's/^Source[0-9][0-9]*: \(.*\/\)\(.*\)/\2: ; curl -f -L -O \1\2 || cp ..\/..\/$(NAME)\/dist\/\2 ./' > deps)

include deps
