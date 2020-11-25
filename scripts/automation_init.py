#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
from subprocess import check_call

if __name__ == '__main__':
    check_call('python scripts/dev_setup.py -p azure-core')
    if len(sys.argv) == 3:
        with open(sys.argv[2], 'w') as file_out:
            file_out.writelines(["{}\n"])

    print("Finished automation init.")
