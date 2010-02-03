#!/usr/bin/python


def valid(obj):
  return (obj == 'a' or obj == 'e' or obj == 'o' or obj=='t' or obj =='T' or obj == 'n' or obj == 'N' or obj == 's' or obj == 'S' or obj == 'c'or obj == 'C' or obj == 'd' or obj == 'D')

def uyir(obj):	
  return (obj >= u"\u0B85" and obj <= u"\u0B94")

def mei(obj):
  return (obj >= u"\u0B95" and obj <= u"\u0BB9")

def uyirmei(obj):
  return (obj >= u"\u0BBE" and obj <= u"\u0BCC")

def convertuyirmei(obj):
  if obj == u"\u0B85":
    return unicode()
  temp = repr(obj)
  temp = "0x" + temp[4:-1]
  try:
    temp1 = hex2dec(temp)
  except ValueError:
  #  print "Error",
    temp1 = 0
  temp2 = temp1-2950+3006
#  temp2 = temp - u"\u0B86" + u"\u0BBE"
  return unichr(temp2)

def hex2dec(s):
  return int(s, 16)
