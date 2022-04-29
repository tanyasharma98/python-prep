import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
num : +91 8957855649
Fax: +1 (703) 243 9791
66-66
455-4545
new_num : +91 5857875878
Email: northamerica@tata.com 
new_num2: +91 6896876786
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''


# findall , search , split , sub , finditter

# sopp = re.compile(r'Moore')
# sopp = re.compile(r'.')
# sopp = re.compile(r'.ew')
# sopp = re.compile(r'^Tata')
# sopp = re.compile(r'iii$')
# sopp = re.compile(r'ai*')
# sopp = re.compile(r'a*i*')
# sopp = re.compile(r'ai+')
# sopp = re.compile(r'ai{2}')
# sopp = re.compile(r'(ai){2}')
# sopp = re.compile(r'(ai){1}')
# sopp = re.compile(r'(ai){1}|Fax')
# sopp = re.compile(r'(ai){1}|Fax')

#Special Sequence
# sopp = re.compile(r'\ATata')
# sopp = re.compile(r'\bTata')
# sopp = re.compile(r'Fax\b')
# sopp = re.compile(r'27\b')
# sopp = re.compile(r'\Bame')


# sopp = re.compile(r'\d{5}-\d{4}')
# matches = sopp.finditer(mystr)
# for match in matches:
#     print(match)
#     # print(mystr[249:254])

#--------------------------------------Task--------------------
#Find INdian phone number start with +91 ,give list

phn = re.compile(r'\B\+91\s\d{10}')
i = 0
matches = phn.finditer(mystr)
for match in matches:
    print(match)
    # listt = [match.group()]
    # listt.append(match)
    # print(listt)

    # listt=[match[:]]

    # print("Here is the list",listt)


