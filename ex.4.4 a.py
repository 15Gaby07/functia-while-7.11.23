n=int(input('Dati un nr.= '))
s4=0
p=1
i=1
while i<=n:
    p*=i
    s4+=(i*10)+2
    i+=1

print('s4=', s4)
