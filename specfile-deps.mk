# generate and include dependencies from the specfile Source*:s
$(shell spectool -l $(NAME).spec | \
        sed -e 's/^Source[0-9][0-9]*: \(.*\/\)\(.*\)/\2: ; \
                curl -L -O \1\2/' > deps)
include deps
