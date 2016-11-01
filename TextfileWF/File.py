from itertools import izip


with open('output','w') as g, open('x') as f, open('x') as o:
    lis=[x.split() for x in f]
    lis2=[m.split() for m in o]
    for x,m in izip(lis,lis2):


            for y in (x):
        
                for i in range(0,31):
                    if i%2==0:

                        print(y[i])
                        g.write(y[i])

            for n in m:
                for i in range(0,31):
                    if i%2==0:
                        g.write(n[i])
            


            g.write('\n')