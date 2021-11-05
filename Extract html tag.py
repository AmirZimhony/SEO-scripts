import xlrd
import xlsxwriter
import requests
import pandas
import sys
from pandas import DataFrame
from bs4 import BeautifulSoup

#helper function, takes care of request, response and making a Beautiful soup object out of a webpage

#@input : URL of a webpage
#@output: Beautiful soup object of the webpage
def MakeSoup(site):
    response = requests.get(site)
    html = response.content
    bsElement = BeautifulSoup(html, "html.parser")
    return bsElement

#load excel file with pages we want to scan
locPages = (r'/Users\Amir\Documents\file.xlsx')#path of file
wbPages = xlrd.open_workbook(locPages)
sheetPages = wbPages.sheet_by_index(0)

workbook = xlsxwriter.Workbook('COMPANY - Viewports.xlsx')#name of file that will contain results
worksheet = workbook.add_worksheet()

for i in range(sheetPages.nrows):
    worksheet.write(i,0,sheetPages.cell_value(i,0))
    site = sheetPages.cell_value(i,0)
    bsElement = MakeSoup(site)
    with open('COMPANY.html', 'wb') as file:
        file.write(bsElement.prettify('utf-8'))
    ##the subjective tag we want to extract, in this case its the "viewport" tag
    viewport = bsElement.find('meta', {'name': 'viewport', })
    worksheet.write(i,1, viewport.get('content') )


workbook.close()