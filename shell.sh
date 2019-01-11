#!/bin/bash

# Do not forget the slash at the end
KHAOS_ROOT="/mnt/d/prog/python/khaosbuild/"

cd $KHAOS_ROOT
source sandbox/bin/activate

export KHAOS_ROOT
export KHAOS_BUILD="${KHAOS_ROOT}build"
export KHAOS_SRC="${KHAOS_ROOT}src"

eval "$(_KHABUILD_COMPLETE=source khabuild)"
eval "$(_KB_COMPLETE=source kb)"

# 
mkdir -p $KHAOS_SRC $KHAOS_BUILD
mkdir -p $KHAOS_BUILD/cache $KHAOS_BUILD/lib $KHAOS_BUILD/include $KHAOS_BUILD/bin
