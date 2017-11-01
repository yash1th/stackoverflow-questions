from sys import *

def open_file(filename):
   data = open(filename, "r").read()
   print (data)

def run():
   data = open_file(argv[1])
   print(data)

run()
