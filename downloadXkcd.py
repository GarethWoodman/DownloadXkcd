#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'             # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

for i in range(5):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status() # If an error is found the download is stopped

    soup = bs4.BeautifulSoup(res.text)
    
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')   # Find img tag/element in comic id
    if comicElem == []:
        print('Could not find comic image.')
    else:
        print(comicElem) # Debugging
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        print(imageFile) # Debugging
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    print(prevLink)
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
