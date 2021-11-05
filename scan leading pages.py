#@input: csv file with a list of pages
#@output: JSON file with lighthouse audit ofor each page we scan
#script for Lighthouse auditing a list of given pages
import csv
import subprocess

count=0;
with open('Leading pages traffic.csv', mode='r') as doc:#open the file as doc
    line=doc.readline()#read first row, irrelevant because its the line with the names of the columns
    for line in doc:#read every row'
        if (count==50):#determine how many pages to audit
            break
        mylist = line.split(",")
        var1,var2,var3,var4,var5 = mylist #split columns to data. first column contains URL of page, thus var1 is used for the lighthouse cmd audit
        print(var1)
        text = 'lighthouse {} --output-path=AutomatedAudits/Company{}.json --output json'.format(var1,count)
        subprocess.call(text, shell=True)
        count+=1





