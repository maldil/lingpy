#! /usr/bin/env python2
# *-* coding:utf-8 *-*
# script needed to compile c-files for development-use

import os

os.system('cython align.pyx')
raw_input('ok')
os.system('gcc -c -fPIC -I/usr/include/python3.3m/ align.c')
os.system('gcc -shared align.o -o align.so')

#raw_input('Successful')
#
#os.system('cython _utils.pyx')
#raw_input('ok')
#os.system('gcc -c -fPIC -I/usr/include/python2.6/ _utils.c')
#os.system('gcc -shared _utils.o -o _utils.so')
#
#raw_input('Successful')
#os.system('cython _cluster.pyx')
#raw_input('ok')
#os.system('gcc -c -fPIC -I/usr/include/python2.6/ _cluster.c')
#os.system('gcc -shared _cluster.o -o _cluster.so')

raw_input('Successful')
