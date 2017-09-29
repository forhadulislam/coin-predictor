import urllib2
from bs4 import BeautifulSoup
import locale

locale.setlocale( locale.LC_ALL, 'english_USA' )
urlContent = urllib2.urlopen('https://coinmarketcap.com/all/views/all/#EUR').read()
soup = BeautifulSoup(urlContent, "html5lib")

imgUrlRoot = "https://files.coinmarketcap.com/static/img/coins/128x128/"



def getCoins():
    data = {}
    for row in soup('table', {'id': 'currencies-all'})[0].tbody('tr'):
        tds = row('td')
        title = tds[2].string.strip()
        data[title] = {}
        
        data[title]['id'] = tds[0].string.strip()
        data[title]['name'] = tds[1]('a')[0].string.strip()
        
        data[title]['image'] = imgUrlRoot + data[title]['name'].lower() + ".png"
        
        #print data[title]
        
        try:
            data[title]['marketCap'] = locale.atof( tds[3].string.strip().replace("$","") )
        except:
            data[title]['marketCap'] = 0
        data[title]['priceUsd'] = locale.atof( tds[4]('a')[0].string.strip().replace("$","") )
        
        try:
            data[title]['totalSupply'] = locale.atof( tds[5]('a')[0].string.strip().replace("$","") )
        except:   
            
            try:
                data[title]['totalSupply'] = locale.atof( tds[5]('span')[0].string.strip().replace("$","") )
            except:
                data[title]['totalSupply'] = 0
            
        try:   
            data[title]['usdVolume'] = locale.atof( tds[6]('a')[0].string.strip().replace("$","") )
        except:
            data[title]['usdVolume'] = 10
        
        
        try:
            data[title]['change1hour'] = float( tds[7].string.strip().replace("%","") )
        except:
            data[title]['change1hour'] = 0
            
        try:
            data[title]['change24hour'] = float( tds[8].string.strip().replace("%","") )
        except:
            data[title]['change24hour'] = 0
            
        try:
            data[title]['change7days'] = float( tds[9].string.strip().replace("%","") )
        except:
            data[title]['change7days'] = 0
    
    
    return data
    
#print data