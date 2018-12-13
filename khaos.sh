#!/bin/bash

KHAOS_ROOT="/home/mazrog/khaos/"

cd $KHAOS_ROOT
source sandbox/bin/activate

export KHAOS_ROOT
export KHAOS_BUILD="${KHAOS_ROOT}build"
export KHAOS_SRC="${KHAOS_ROOT}src"

eval "$(_KHABUILD_COMPLETE=source khabuild)"
alias kb="khabuild"

# 
mkdir -p $KHAOS_SRC $KHAOS_BUILD
mkdir -p $KHAOS_BUILD/cache $KHAOS_BUILD/lib $KHAOS_BUILD/include $KHAOS_BUILD/bin
