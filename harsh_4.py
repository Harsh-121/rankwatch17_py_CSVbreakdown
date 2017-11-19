from glob import glob
import csv

files=glob('raw/*.csv')

for x in files:
    with open(x,'r') as f:
        data=csv.reader(f, delimiter=',')
        for row in data:
			if len(row) > 1:
				# name of the processed file to save data 
				name=row[0]+'-processed.csv'
				# data to save in the processed file
				text=row[1:]
				text=','.join(text)
				text=text+'\n'
				with open('processed/'+name,'a') as nf:
					nf.write(text)
