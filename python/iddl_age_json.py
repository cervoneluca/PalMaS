#!/usr/bin/env python

import argparse
import string
import Image, ImageOps
import logging
import urllib
import csv
import time
import calendar
import json
from datetime import datetime
from urlparse import urlparse


# Main ########################################################################
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('csv_read', help='file csv sorgente')
  parser.add_argument('dataPresentazione', help='n colonna', type=int)
  parser.add_argument('dataApprovazione', help='n colonna', type=int)
  parser.add_argument('json_write', help='path del json da produrre')
  args = parser.parse_args()
  
  csvfile = open(args.csv_read, 'r')
  jsonfile = open(args.json_write, 'w')

  fieldnames = next(csv.reader(csvfile))
  
  reader = csv.DictReader(csvfile, fieldnames)
  for row in reader:
    #row['age']='age'
    #row['dataPresentazioneTS']='dataPresentazioneTS'
    #row['dataApprovazioneTS']='dataApprovazioneTS'
    #t0 = datetime.strptime(row[args.dataPresentazione], '%Y-%m-%d')
    #t1 = datetime.strptime(row[args.dataApprovazione], '%Y-%m-%d')
    #diff = t1 - t0
    #row.append(diff.days)
    #row.append(calendar.timegm(t0.utctimetuple()))
    #row.append(calendar.timegm(t1.utctimetuple()))
    
    json.dump(row, jsonfile)
    jsonfile.write('\n')
  
  #with open(args.csv_read, 'rb') as csvfile:
  #  reader = csv.reader(csvfile)
    
  #  jsonfile = open(args.json_write, 'w')
    
    #fieldnames = next(reader)
    
    #json.dump(fieldnames, jsonfile)
    
        
    #for row in reader:
    #    
    #    
        
    #    
    #    
        
        
    #    
    #    
        #c.writerow(row)
