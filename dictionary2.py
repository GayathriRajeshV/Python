d1={"A":"a","B":"b"}
d2={"C":"c","D":"d"}
d3={"E":"e","F":"f"}
d4={}
for d in(d1,d2,d3):d4.update(d)
print(d4)

c1={"Meera":51,"Krishna":78,"Ram":48,"Mansi":50,"Bhumi":45}
c1_sort=sorted(c1, key=c1.get, reverse=True)
for r in c1_sort:
    print(r,c1[r])
    
a=open("file1.py")
f=a.read()
print(len(f))


