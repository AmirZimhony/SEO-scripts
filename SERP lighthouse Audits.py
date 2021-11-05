#Script for extracting JSON lighthouse audits for 10 different pages (SERP of certain query)
import subprocess  #ENABLE CMD ACTIONS
import re  #Short for regex

SiteList={}
SiteList["1"]='https://www.max.co.il/loans/calc'
SiteList["2"]='https://www.cal-online.co.il/ecredit/instant-loan/'
SiteList["3"]='https://digital.isracard.co.il/digital-loans/main/'
SiteList["4"]='https://www.bankjerusalem.co.il/loans'
SiteList["5"]='https://www.eloan.co.il/'
SiteList["6"]='https://www.5555.co.il/'
SiteList["7"]='https://www.bank-yahav.co.il/%D7%94%D7%92%D7%A9%D7%AA_%D7%91%D7%A7%D7%A9%D7%AA_%D7%94%D7%9C%D7%95%D7%95%D7%90%D7%94.aspx'
SiteList["8"]='https://www.mizrahi-tefahot.co.il/he/bank/loans-category/pages/default.aspx'
SiteList["9"]='https://www.wobi.co.il/%D7%94%D7%9C%D7%95%D7%95%D7%90%D7%94/'
SiteList["10"]='https://www.leumi.co.il/Lobby/loans/35622/'
test=SiteList["7"][8:]#filter out first 8 characters of each string ("https://" in this case)
print(re.match("(.*?)il",test).group())
#scan all 10 websites
for x in range(10):
    y=str(x+1)
    text = 'lighthouse {} --output-path=AutomatedAudits/{}5.json --output json'.format(SiteList[str(y)],re.match("(.*?)il",SiteList[str(y)][8:]).group())#regex command to filter out unnecessary parts of url(after "il")
    subprocess.call(text, shell=True)