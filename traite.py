#coding:utf-8
import os

f=open("main.py","r")
txt=f.read()
f.close()

f=open("main.py","w")
f.write(txt.replace("\t","    "))
f.close()
