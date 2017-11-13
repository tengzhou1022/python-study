import sys, string

f = open("test.log","w")
sys.stdout = f
help(string)
f.close()
