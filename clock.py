h=0
for h in range(24):
    for m in range(60):
     for s in range(60):
         for d in range(10000000):
               if d==9999999:
                print("\r", (format(str(h)+"  :  "+str(m)+"  :  "+str(s)).center(60)), end='')