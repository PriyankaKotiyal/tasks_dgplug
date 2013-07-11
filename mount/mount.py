#!/usr/bin/env python
f = open("/proc/mounts")
print f.read()
f.close()
