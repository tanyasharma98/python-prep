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

# patt = re.compile(r'fass')
# patt = re.compile(r'.lekin')
# patt = re.compile(r'^Tata'
# patt = re.compile(r'ii$')
# patt = re.compile(r'ii{4}')
# patt = re.compile(r'Di|ons')
# patt = re.compile(r'(ta)')
"""Special sequence"""

# patt = re.compile(r'\ATata')
# patt = re.compile(r'\bFax')
# patt = re.compile(r'mi\b')
patt = re.compile(r'\d{2}\s\d{10}')

matches = patt.finditer(mystr)
lst = []

for match in matches:
    lst.append(match)
    print(match)
print(lst[1])
# print(mystr[580: 582])
