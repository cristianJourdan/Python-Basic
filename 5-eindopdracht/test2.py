import time

sec = int(input("aantal Seconden: "))
minuten = int(input("aantal minuten:"))
uren = int(input("aantal uren:"))


# def klok(u, m ,s):
#     sstr = str(s)
#     mstr = str(m)
#     ustr = str(u)
#     if u < 10:
#          ustr = "0" + ustr
#          mstr = str(m)
#     if m < 10:
#         mstr = "0" + mstr
#         sstr = str(s)
#     if s < 10:
#         sstr = "0" + sstr
#     tstr = ustr + ":" + mstr + ":" + sstr
#     print (tstr)
#     time.sleep(1)
#     return

for u in range(uren,25):
    
    for m in range(minuten,61):
        
        for s in range(sec,60):
            time.sleep(1)
            print (str(u)+":"+ str(m)+":"+ str(s))
            if(m == 60):
                    m = 0
            if(s == 59):
                sec = 0
            if(u == 24):
                    u = 0
               

            
 
    
             

    


        


