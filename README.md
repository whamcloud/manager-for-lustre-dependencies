# manager-for-lustre-dependencies

[![Build Status](https://travis-ci.org/intel-hpdd/manager-for-lustre-dependencies.svg?branch=master)](https://travis-ci.org/intel-hpdd/manager-for-lustre-dependencies)

Dependencies needed for IML not available elsewhere.

## Overview

This repo is organized such that each directory cooresponds to a dependency. 

The dependencies are reflected in our [copr project](https://copr.fedorainfracloud.org/coprs/managerforlustre/manager-for-lustre/).

This decouples our dependency code from our application code. We can also package our application using this process.

## Updating dependencies

There are a few steps needed to update a dependency.

In the directory you want to update:

1. Upload a `.tgz` file cooresponding to the version you want to change
2. Update the `.spec` file.
3. Upload your change as a PR and pass review.
4. Tag your change using [tito](https://github.com/dgoodwin/tito): `tito tag --no-auto-changelog --keep-version`
5. Push your change, a gatekeeper will land, and a build will be kicked off.

