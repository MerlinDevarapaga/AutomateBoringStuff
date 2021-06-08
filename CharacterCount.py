
import pprint

messsage='It was a bright cold day in April, and the clocks were stricking Thirteen'
count={}#'r':12

for character in messsage.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1

print('This print is normal print function')
print(count)

print('This print is done by pprint method')
pprint.pprint(count)


print('This print is done by pformat method to store in string format')
rjtext=pprint.pformat(count)
print(rjtext)
