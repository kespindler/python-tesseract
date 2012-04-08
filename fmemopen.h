extern "C"  {
/*
 * fmem.h : fmemopen() on top of BSD's funopen()
 * 20081017 AF
 */

#ifndef _FMEM_H
#define _FMEM_H

#ifndef linux
#include <stdio.h>
extern FILE *fmemopen(void *buf, size_t size, const char *mode);
#else
#define _GNU_SOURCE
#endif

#endif /* fmem.h */
}
