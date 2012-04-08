# Python Wrapper Class for Tesseract
### (Linux & Mac OS X & Windows)
It is a wrapper class for Tesseract OCR. Python-tesseract allows any conventional image file (JPG, GIF ,PNG , TIFF and etc) to be read and decoded into readable languages. No temporary file will be created during the OCR processing.

#### Example:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #from __future__ import print_function

    import tesseract
    api = tesseract.TessBaseAPI()
    api.Init(".","eng",tesseract.OEM_DEFAULT)
    api.SetPageSegMode(tesseract.PSM_AUTO)


    mImgFile = "eurotext.jpg"
    mBuffer=open(mImgFile).read()
    result = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
    print "result(ProcessPagesBuffer)=",result
