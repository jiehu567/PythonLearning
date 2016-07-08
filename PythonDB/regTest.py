# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:22:26 2016

@author: hujie
"""

import re

email = "jhu10@horizon.csueastbay.edu"

org = re.findall(r"@(\S+?)\.", email)
org = str(org)[2:-2]
print org