#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from icecream import install
from icecream import ic

install()

ic.configureOutput(includeContext=True)

from B import foo

if __name__ == "__main__":

    ic("Hello World")
    foo()