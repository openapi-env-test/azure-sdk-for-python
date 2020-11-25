#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
from subprocess import call
import os


def myPrint(info):
    print('XXXXXXXXXXXXXXX:' + info)


if __name__ == '__main__':
    call('python scripts/dev_setup.py -p azure-core', shell=True)
    myPrint('len(sys.argv):' + len(sys.argv))
    if len(sys.argv) == 3:
        myPrint('sys.argv[2]:'+sys.argv[2])
        with open(sys.argv[2], 'w') as file_out:
            file_out.writelines(["{}\n"])
            myPrint('output succeed!!!')

    print("Finished automation init.")
