# run like: /usr/bin/python create_comparisons.py>comparisons.txt

from itertools import combinations

#l=["9925_9935","9550_9555","7094_7287","1254_8351","9518_9522","768_772","9402_9416","9725_9726","7025_7067","22010_18516","22002_18514","22001_22000","22007_21999", "18515_35614", "9764_9762"]
# new list controlling for admixture
#l=["9847_9941","9555_9600","7014_9442","9522_9547","9726_9991","7067_9727","22010_18516","22002_18514","22001_22000","22007_21999", "18515_35614"]
# eurasian list
#l=["9925_9935","768_77"]
l=["9925_9935","9550_9555","7094_7287","1254_8351","9518_9522","768_772","9402_9416","9725_9726","7025_7067","22010_18516","22002_18514","22001_22000","22007_21999", "18515_35614", "9764_9762", "AH0001_AH0002", "AH0007_AH0008", "35520_211399", "9764_9761"]


#for i in combinations(l, 2):
#    print i[0]+"x"+i[1]

#for i in combinations(l, 2):                                                                          #    if "18515_35614" in i:
#        print i[0]+"x"+i[1]   

#for i in combinations(l, 2):
#    if any(comp in ["AH0001_AH0002","AH0007_AH0008"] for comp in i):
#        print i[0]+"x"+i[1]

for i in combinations(l, 2):
    if "9764_9761" in i:
        print i[0]+"x"+i[1]
