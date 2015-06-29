import array
c=array.array('f',(0 for i in range(0,100)))
lista={}
c[0]=1
c[1]=1
index=1
while index<99:      
    c[index+1]=c[index]+c[index-1]
    index =index +1
for i in c:
    print "%.0f" %i
print "Numero PHI: ",c[index]/c[index-1]
