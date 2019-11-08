Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
print ("Length : %d" % len (Dict))
print("printable string:%s" % str(Dict))
for S in Students:
      print(' ' "::"' ' .join((S,str(Dict[S]))))
      # print("printable string:%s" % str(Dict))