import imapclient, bs4, pyzmail, re, webbrowser

# Log in to email account
imapObj = imapclient.IMAPClient('imap.aol.com', ssl=False)
imapObj.login('gareth_woodman@aol.com', '1competent1')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search()

# Loop through all emails
for i in UIDs:
    rawMessages = imapObj.fetch([i], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])
    try:
        msgSubject = message.get_subject()
        print(msgSubject)

        for l in range(5):
            print('-----------------------')
			
        htmlObj = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(htmlObj)
        listA = soup.findAll('a')

        # Find words matching unsubscribe
        regex = re.compile(r'unsubscribe', re.I)

        # Loop through all a tags
        for i in listA:
            strP = str(i)
            try:
                p = regex.search(strP)
                if p != None:
                    print(i)
                    url = i.get('href')
                    webbrowser.open(url)
                    
                else:
                    print('no link')
            except:
                print('no good')
                
    except:
        print('No More content')
