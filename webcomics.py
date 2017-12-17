#Hwee Lee
#Python 2.7
#Code is written for specific comics and knowledge of how comics are structured
#i.e. xkcd comics have alt text 

import requests , os , bs4 
    
#Links to main page for webcomics
url = ['http://xkcd.com' , 'http://buttersafe.com' , 'http://nedroid.com' , 'http://theawkwardyeti.com']

#global arrays to save comic title, image link, and alt text
comicTitle = []
comicImg = []
comicAltText = []

#Download pages for webcomics and source information
for i in range (0 , len(url)):
    res = requests.get(url[i])
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.content , "html.parser")  
    comicElem = soup.select('#comic img')

    

    comicTitle.append(comicElem[0].get('alt'))   
    comicImg.append(comicElem[0].get('src'))
    comicAltText.append(comicElem[0].get('title'))


#open html file for writing
comicsFile = open(os.path.join('desktop' , 'SundayComics.html') , 'wb')
comicsFile.write('<html> <Head> <Title> Comic Digest </Title> </Head> ')

# Write comics into one file
for i in range (0 , len(url)):
    
    #Checks to see if source links includes http: , appends http: if it does not
    if(comicImg[i][0] != 'h'):
        comicImg[i] = 'http:' + comicImg[i]
        
    comicsFile.write('<header> <h1>' + comicTitle[i] + "</h1> <header>")
    comicsFile.write('<body> <img src = ' + comicImg[i] + '>')
    
    if comicAltText[i] != None:
        comicsFile.write('<br> <i>' + comicAltText[i] + ' </i> <br> </body>')
    
        
comicsFile.write('</html>')
comicsFile.close()



print('Finished')


