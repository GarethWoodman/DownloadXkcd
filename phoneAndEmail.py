#! python3
# phoneAndEmail.py - Finds phone numbers and email address on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?         # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)          # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4}){1,2}
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for i in phoneRegex.findall(text):
    print(i)
    phoneNum = '-'.join([i[1], i[3], i[5]]) #phoneNum = xxx-xxx-xxxx
    if i[8] != '':
        phoneNum += ' x' + i[8]
    matches.append(phoneNum)
for i in emailRegex.findall(text):
    matches.append(i[0])
    print(i)

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
#phoneMo = phoneRegex.findall(str(pyperclip.paste()))
#emailMo = emailRegex.findall(str(pyperclip.paste()))

#print('\n'.join(matches))

#for i in range(len(phoneMo):
               #print(phoneMo[i])
