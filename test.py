#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import print_function
import tesseract
import ctypes
import os
#print "HAVE_LIBLEPT=",tesseract.isLibLept()
#print dir("tesseract")
#print tesseract.MAX_NUM_INT_FEATURES
api = tesseract.TessBaseAPI()
api.SetOutputName("outputName");
#api.Init(".","eng")
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)
mImgFile = "eurotext.jpg"

result = tesseract.ProcessPagesWrapper(mImgFile,api)
print "result(ProcessPagesWrapper)=",result
#api.ProcessPages(mImgFile,None, 0, result)
#print "abc"
result = tesseract.ProcessPagesFileStream(mImgFile,api)
print "result(ProcessPagesFileStream)=",result

result = tesseract.ProcessPagesRaw(mImgFile,api)
print "result(ProcessPagesRaw)",result

mBuffer=open(mImgFile).read()
result = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
print "result(ProcessPagesBuffer)=",result
