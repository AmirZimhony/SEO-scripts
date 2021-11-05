#script for transferring data from multiple JSON files (lighthouse audits) to a condensed excel file with all the 
#relevant scores of each page that was audited
#@input: multiple JSON files of lighthouse audits
#@output: an excel file with the speed data of each page that was audited
import json
import xlsxwriter


workbook = xlsxwriter.Workbook('speed results Company.xlsx')
worksheet = workbook.add_worksheet()
col = 0
for x in range(50):#for all json reports with a different index, assuming we have 50 audits
    row = 0
    with open('COMPANY{}.json'.format(x), encoding="utf8") as j:  #open the file as doc
        data = json.load(j)
        print(data['audits']['interactive']['score'])
        print(data['audits']['speed-index']['score'])
        print(data['audits']['first-contentful-paint']['score'])
        print(data['audits']['first-cpu-idle']['score'])
        print(data['audits']['first-meaningful-paint']['score'])
        print(data['audits']['max-potential-fid']['score'])
        scores = (
        ['Interactive', data['audits']['interactive']['score']],
        ['Speed-Index',   data['audits']['speed-index']['score']],
        ['First contentful paint',  data['audits']['first-contentful-paint']['score']],
        ['First CPU idle',  data['audits']['first-cpu-idle']['score']],
        ['First meaningful paint', data['audits']['first-meaningful-paint']['score']],
        ['MAX potential FID', data['audits']['max-potential-fid']['score']],
        )
        print(scores)
        for dimension, result in (scores):
            worksheet.write(row, col, result)
            row += 1
        col += 1
workbook.close()