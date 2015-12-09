list=[]
for i in range(1,8):
   if i < 3:
      list.append(1)
   else: 
      i = list [-1]+list[-2]
      list.append(i)
      print list