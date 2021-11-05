#------------------script for extracting the most common queries leading to certain pages on google search
#------------------2 files are necessary: one with pages, one with info of queries/pages (get them both from Google search console)
#script checks each page in "info" file to see it it is on the list of webpages on "pages" file, if this is the case it adds
# the corresponding query to the list of the corresponding webpage
import xlrd
import xlsxwriter


workbook = xlsxwriter.Workbook('QueriesOfPagesDirectChannels.xlsx')
worksheet = workbook.add_worksheet()
locPages = ('/Users\Amir\Documents\Work\PagesOfSite')
locInfo = ('/Users\Amir\Documents\Work\queriesAndPagesOfSite')

DictOfPages = []
wbPages = xlrd.open_workbook(locPages)
sheetPages = wbPages.sheet_by_index(0)

wbInfo = xlrd.open_workbook(locInfo)
sheetInfo = wbInfo.sheet_by_index(0)


for i in range(sheetPages.nrows):
    DictOfPages.append(sheetPages.cell_value(i,0))
print(DictOfPages)
DictOfPages = dict.fromkeys(DictOfPages)
for key in DictOfPages:
    DictOfPages[key] = []

for i in range(1441):#determine number of queries to scan
    if sheetInfo.cell_value(i, 1)  in DictOfPages:
        DictOfPages[sheetInfo.cell_value(i, 1)].append(sheetInfo.cell_value(i, 0))

i = 0
for key in DictOfPages:
    worksheet.write(i,0, key)
    worksheet.write(i, 1, str(DictOfPages[key]))
    i = i+1

workbook.close()
