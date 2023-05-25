# -*- coding: utf-8 -*-
""" setup.py; setuptools control. """

from setuptools import setup

with open("readme","rb") as f:
   long_descr= f.read().decode("utf-8")

setup(
  name= "dmr_analysis",
  packages= [
     "dmr_analysis",
     "dmr_analysis.script",
     "dmr_analysis.script.script_high",
     "dmr_analysis.script.script_high.others"],
  entry_points = {
     "console_scripts": ['dmr_analysis = dmr_analysis.dmr_analysis:main']} ,

  )
 
