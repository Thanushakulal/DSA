#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if 2<=n<=5:
        if n%2==0:
            print("Not Weird")
        else:
            print("Weird")
    elif 6<=n<=20:
        if n%2==0:
            print("Weird")
        else:
            print("Weird")
    elif n>20:
        if n%2==0:
            print("Not Weird")
        else:
            print("Weird")
    elif n%2!=0:
        print("Weird")
