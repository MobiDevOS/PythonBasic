#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime

if __name__ =="__main__":
    now = datetime.datetime.now()
    hour = now.strftime('%H')
    hourInt = int(hour)
    if hourInt>=0 and hourInt<10 :
        print(10)
    elif hourInt>=10 and hourInt<=20:
        print(20)
    else:
        print(10)


