while True:
    i=0
    sum_n=0
    sum_u=0
    while i<3:
        x=int(input("enter a num"))
        sum_n=sum_n+x
        m=int(input("enter a num"))
        sum_u=sum_u+m
        i+=1
    avr=sum_n/sum_u
    print ("avr=" , avr)
    if avr==20:
        break
print("finish")
