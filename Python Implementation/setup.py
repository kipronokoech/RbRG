#!/usr/bin/env python
import sys
# sys.path.append('/home/philipe/.pyenv/versions/3.5.1/lib/python3.5/site-packages')
# sys.path.append("/home/philipe/Documents/Bit_repositories/Django/label-interface/rango")

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("callRGR",
                             sources=["callRGR.pyx", "RGRmain.cpp"],
                             include_dirs=[numpy.get_include()])],
)