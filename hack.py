txt = """"""

urls = txt.splitlines()
#print(urls)
count=0
total=0
useful_urls=[]
for url in urls:
    total+=1
    x = url.split('/')
    #print(x)
    if x[4]!='ug' and x[4]!='zh-hans':
        useful_urls.append(url)
        count+=1

for i in useful_urls:
    print(i)

print(count,' useful URLs out of ',total)
