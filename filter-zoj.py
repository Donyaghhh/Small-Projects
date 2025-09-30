#filter<zoj<list
a=[5,2,10,12,25,18,15,66]
zoj_numbers=[]
i=0
while i<len(a):
    if a[i] % 2 == 0 :
        zoj_numbers.append(a[i])
    i+=1
print ("zoj_number=" , zoj_numbers)
