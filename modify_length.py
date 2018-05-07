#-*- coding:utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt 
import scipy.io as sio
import os.path as osp
import random, os
import cv2
import cPickle as cp
import scipy.signal as ssig
import scipy.stats as sstat
import pygame, pygame.locals
from pygame import freetype
#import Image
from PIL import Image
import math
from common import *
from random import randint
import codecs

rp_path='/home/chenqiyuan/PycharmProjects/SynthText_Chinese_version/data/newgroup_modify/'
fn='/home/chenqiyuan/PycharmProjects/SynthText_Chinese_version/data/newsgroup/'

files= os.listdir(fn)
for filename in files:
    print filename
    fc=filename
    write_path=rp_path+fc
    fc=fn+fc
    print fc
    with codecs.open(fc,'r','utf-8') as f:
        f2=codecs.open(write_path,'w', 'utf-8')
        print write_path
        for l in f.readlines():
            line=l.strip()
            #line=line.decode('utf-8')
            # print line
            for i in range(len(line)):
                tl=randint(1,5)
                if i + tl<len(line):
                    f2.write('%s\n'%line[i:i+tl])
                else:
                    f2.write('%s\n'%line[i:])
