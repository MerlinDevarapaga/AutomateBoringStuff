import  re
message= ' call me 415-528-0000 tomorrow or at 457-985-5252'

#--------------------------------------------------------------Type 1-------------------------------------#

phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#defining and storing the re expression object
matchObject=phoneNumRegex.search(message)  # search fun to search the pattern
print(phoneNumRegex.search(message).group()) #return the first seearch number --> using group() method
print(matchObject.group()) 
print(phoneNumRegex.findall(message)) #To find all the searches of Numbers in the given input

#--------------------------------------------------------------Type -------------------------------------#

phoneNumRegex2=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')#defining and storing the re expression object using () to group the code and number
matchObject2=phoneNumRegex2.search(message)  # search fun to search the pattern
print(matchObject2.group(1))  # Divides  in to groups if we use () () () in the re expression object
print(matchObject2.group(2))
print(matchObject2.group(3))
print(matchObject2.group(0)) #group(0) return whole matching string


#--------------------------------------------------------------Type -------------------------------------#
message2= ' call me (415) 528-0000 tomorrow or at 457-985-5252'
phoneNumRegex3=re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')#defining to find also the paranthisis "\(and \)" present in the given input
print(phoneNumRegex3.search(message2).group())


#pipe charachter used to match one of the many variables
BatRegex=re.compile(r'Bat(man|mobile|copter|bat)')
matchObject2=BatRegex.search('Batmobile lost a wheel')
print(matchObject2.group())
