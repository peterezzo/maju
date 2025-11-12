# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Pete Ezzo

import time

def nap(delay: float = 60.0 * 60 * 36):
    print('Taking a nap')
    time.sleep(delay)
    raise SystemExit
