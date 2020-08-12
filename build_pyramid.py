#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:29:50 2020

@author: eason
"""


from mcpi.minecraft import Minecraft 
mc = Mi
x,y,z = mc.player.gnecraft.create()etPos()
base = 10
height = base//2+1

for i in range(height):
    x1 = x+i
    y1 = y+i
    z1 = z+i
    
    x2 = x+base-i
    
    z2 = z+base-i
    mc.setBlocks(x1,y1,z1,x2,y1,z2,41)