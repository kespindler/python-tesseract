#!/usr/bin/env python

"""
setup.py file for SWIG
written by FreeToGo@gmail.com
"""
from distutils.core import setup, Extension
import sys,os
incl=os.path.join(sys.prefix,"include")
version_number=os.getcwd().split("-")[-1]
print "Current Version : %s"%version_number

def inclpath(mlib):
	return os.path.join(incl,mlib)
	
tesseract_module = Extension('_tesseract',
									sources=['tesseract.i', 'main_dummy.cpp',],
									swig_opts=["-c++", "-I"+inclpath('tesseract'),
													"-I"+incl,
													"-I"+inclpath('leptonica')],
									include_dirs=['.',inclpath('tesseract'),
													incl,
													inclpath('leptonica')],
									libraries=['stdc++','tesseract_api','lept']
									)
									
setup (name = 'python-tesseract',
       version = version_number,
       author      = "FreeToGo",
       description = """${python:Provides} Wrapper for Python-${python:Versions} """,
       ext_modules = [tesseract_module],
       py_modules = ["tesseract"],
  #     data_files=[('.',['test.py','eurotext.tif','eurotext.jpg']),],
       )
       
