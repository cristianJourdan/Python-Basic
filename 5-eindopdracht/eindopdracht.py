
import time
seconden = input("Sec: ")
s = int(seconden)
minuut = input("minuut:")
m = int(minuut)
uur = input("uur:")
h = int(uur)
while (s < 60):
    print ("uren:"+str(h) +" "+ "minuten:"+ str(m)+" "+ "seconden:" + str(s)) 
    time.sleep(1)
    s=s+1
    if (s == 60):
        m=m+1
        s = 0

    elif(m == 60):
        h=h+1
        m = 0
        s = 0
    
    elif(h == 24):
        h = 0
#copyright *Cristian Jourdan*




