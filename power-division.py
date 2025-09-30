#devision-fard-list
a=[5,8,10,12,18,17,28,13,38,3]
d_fard=[]
s_zoj=[]
i=0
while i<len(a):
    if a[i] % 2 ==0:
        s_zoj.append(a[i]**2)
        i+=1
    else:
        d_fard.append(a[i]/4)
        i+=1
print ("zoj_number=" , s_zoj , "fard_number=" , d_fard)
