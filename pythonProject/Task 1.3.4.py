x=int(input("Арабское число: "))
b=["",'I','II','III','IV','V','VI','VII','VIII','IX','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C','CX','CXX','CXXX','CXL','CL','CLX','CLXX','CLXXX','CXC','CC','CCC','CD','D','DC','DCC','DCCC','CM','M']
d=["",'X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
e=["",'C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
if x in range(1,1000):
    print(e[int((((int(x/100))*100)-1000)/100)]+d[int((x-(int(x/100)*100))/10)]+b[((x%1000)%100)%10])
if x==1000:
    print(b[37])
if x in range(1001,2000):
    print(b[37]+e[int((((int(x/100))*100)-1000)/100)]+d[int((x-(int(x/100)*100))/10)]+b[((x%1000)%100)%10])
if x==2000:
    print("MM")
if x in range(2001,3000):
    print(b[37]+b[37]+e[int((((int(x/100))*100)-2000)/100)]+d[int((x-(int(x/100)*100))/10)]+b[((x%1000)%100)%10])
if x==3000:
    print("MMM")
if x in range(3001,4000):
    print(b[37]+b[37]+b[37]+e[int((((int(x/100))*100)-3000)/100)]+d[int((x-(int(x/100)*100))/10)]+b[((x%1000)%100)%10])
if x not in range(1,4000):
    print("Error")