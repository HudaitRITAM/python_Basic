from array import *
vals=array('i',[7,9,3,8])
newarr=array(vals.typecode,(a*a for a in vals)) #for copying old element to new arr element in sqrt form
for e in newarr:
 print(e)