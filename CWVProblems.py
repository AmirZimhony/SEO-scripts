#script for reading site CWV-relevant data from a JSON file 
import json


with open(r'C:\Users\Amir\Downloads\input.json', encoding="utf8") as j:  #open the file as doc
    data = json.load(j)

# ------------print URL of requested page------------------
    print('\n The page with the CWV issues is:')
    print(data['requestedUrl'])

    # ------------eliminate render-blocking resources------------------
    renderBlockingResources = data['audits']['render-blocking-resources']['details']['items']
    print('\n render-blocking resources: URL, total bytes, wasted Ms')
    for item in renderBlockingResources:
        print(item['url'], " , " + str(item['totalBytes']) , " , " + str(item['wastedMs']))


    # ------------Redundant CSS------------------
    redundantCSS = data['audits']['unused-css-rules']['details']['items']
    print('\n redundant CSS: URL, total bytes, wasted bytes, wasted percent')
    for item in redundantCSS:
        print(item['url'], " , " + str(item['totalBytes']) , " , " + str(item['wastedBytes']), " , " + str(item['wastedPercent']))
    

    # ------------Redundant JS------------------
    redundantJS = data['audits']['unused-javascript']['details']['items']
    print('\n redundant JS:URL, total bytes, wasted bytes, wasted percent')
    for item in redundantJS:
        print(item['url'], " , " + str(item['totalBytes']) , " , " + str(item['wastedBytes']), " , " + str(item['wastedPercent']))
    
    # ------------Require pre-load------------------
    requirePreLoad = data['audits']['uses-rel-preload']['details']['items']
    print('\n require Pre-Load:')
    for item in requirePreLoad:
        print(item['url'])

    # ------------unsized images------------------    
    unsizedImages = data['audits']['unsized-images']['details']['items']
    print('\n Unsized images:')
    for item in unsizedImages:
        print(item['url'])

# ------------unminified CSS------------------    
    unminifiedCSS = data['audits']['unminified-css']['details']['items']
    print('\n unminified CSS:URL, total bytes, wasted bytes, wasted percent')
    for item in unminifiedCSS:
        print(item['url'], " , " + str(item['totalBytes']) , " , " + str(item['wastedBytes']), " , " + str(item['wastedPercent']))

# ------------requires text compression------------------    
    textToCompress = data['audits']['uses-text-compression']['details']['items']
    print('\n text files to compress: URL, total bytes, wasted bytes')
    for item in textToCompress:
        print(item['url'], " , " + str(item['totalBytes']) , " , " + str(item['wastedBytes']))
         

   


