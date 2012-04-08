import platform

osname=platform.uname()[0].lower()
fp=open("config.h","w")
fp.write("#ifndef __%s__\n"%osname)
fp.write("\t#define __%s__\n"%osname)
fp.write("#endif\n")
fp.close()
