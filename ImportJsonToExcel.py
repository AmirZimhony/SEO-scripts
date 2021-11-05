#script for reading site speed-relevant data from a JSON file (JSON is output from Google Lighthouse audit) and printing it to excel file
import csv
import json
import xlsxwriter
import requests
from datetime import date

workbook = xlsxwriter.Workbook('speed results 23 feb.xlsx')
worksheet = workbook.add_worksheet()

with open('23 feb.json', encoding="utf8") as j:  #open the file as doc
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
    row = 0
    col = 0
    for dimension, result in (scores):
        worksheet.write(row, col, dimension)
        worksheet.write(row, col + 1, result)
        row += 1

workbook.close()

