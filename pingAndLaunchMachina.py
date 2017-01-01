#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import time
import sys


def pingOk(sHost):
    try:
        output = subprocess.check_output("ping -c 1 "+sHost, shell=True)
    except Exception, e:
        return False

    return True

if __name__ == '__main__':
    notLaunched = True
    hostname = "www.google.com"  # example
    while notLaunched:
        if pingOk(hostname):
            print "It's on!"
            time.sleep(5)
            sys.exit()
