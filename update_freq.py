from collections import Counter
import pickle
import os
cnt=0
filepath ='/home/chenqiyuan/PycharmProjects/SynthText_Chinese_version/data/newsgroup'
files= os.listdir(filepath)

for file in files:
    with open(os.path.join(filepath,file)) as f:
        c = Counter()
        for x in f:
            x=x.decode('utf-8')
            c += Counter(x.strip())
            cnt+=len(x.strip())
        #print c
print cnt

for key in c:
    c[key]=float(c[key])/cnt  
    print key,c[key]
     
d = dict(c)
#print d
with open("char_freq.cp",'wb') as f:
    pickle.dump(d,f)
