#! python3

import  re, pyperclip

# Create a regex for Phone number

phoneRegex=re.compile(r'''
#415-555-5255,666-0000, (415) 555-0000, 555-0000 ext 12345,ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\d\))?               #areacode(optional))
(\s|-)                                   #first sepeartor
\d\d\d                                   #first 3 digits
 -                                       #seperator
\d\d\d\d                                 #last 4 digits
((ext(\.)?\s)|x)                        #extension word part (optional)
(\d{2,5}))?                              #extension number pattern (optional)

)
''',re.VERBOSE)

#Create a regex for email address


emailRegex=re.compile(r'''
#some.+_thing @somthing .com

[a-zA-Z0-9_.+]+      #name part
@                    #@ symbol
[a-zA-Z0-9_.+]+      #domain name part


''',re.VERBOSE)


# Get the text off the clipboard

text=pyperclip.paste()


# Extract the email/phone form this text

extractedPhone=phoneRegex.findall(text)
extractedEmail=emailRegex.findall(text)

allPhoneNumbers=[]
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])



# TODO: Copy the extracted email/phone to the clip board

results= '\n'.join(allPhoneNumbers) +'\n'+'\n'.join(extractedEmail)
pyperclip.copy(results)

