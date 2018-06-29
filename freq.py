import matplotlib.pyplot as plt
import numpy as np


def freq(x):
	x=x.lower()
	x.replace(" ","")
	word_count={}
	for i in range(len(x)):
		sym = x[i]
		if(sym>'a' and sym<'z' or sym>'A' and sym<'Z'):
			if(sym in word_count.keys()):
				word_count[sym]+=1
			else:
				word_count[sym]=1
	return word_count

def get_freq(file_name):
	fo=open(file_name,"r+")
	str=fo.read()
	w_frequncies= freq(str) # run the frequency counter on this file's data
	fo.close()
	return w_frequncies

fname = raw_input("Enter file name(xyz.txt):")
data=get_freq(fname)

plt.bar(range(len(data)), list(data.values()), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.show()
