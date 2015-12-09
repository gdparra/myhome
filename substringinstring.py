
mystring =" I rock your world word rock"
mylist=mystring.split()
print mylist
mynewlist=[]
for i in mylist:
       if i not in mynewlist:
          mynewlist.append(i)

print mynewlist