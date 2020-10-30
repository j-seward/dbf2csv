#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:17:39 2019

@author: Jonathan Seward

Program: This program converts a database file (.dbf) to a comma separated file
    (.csv) since most statistical software packages don't use .dbf anymore. To 
    use, you drop this in the folder with your .dbf files and run.
"""

#!/usr/bin/python

import csv
from dbfpy import dbf
#import os
import sys

filename = sys.argv[1]
if filename.endswith('.dbf'):
    print ("Converting %s to csv") % filename
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csvfile:
        in_db = dbf.Dbf(filename)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields:
            names.append(field.name)
        out_csv.writerow(names)
        for rec in in_db:
            out_csv.writerow(rec.fieldData)
        in_db.close()
        print ("Done...")
else:
  print ("Filename does not end with .dbf")