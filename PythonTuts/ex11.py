#Email Collector

import  re
str="""
fdknhfklnd hflaskf ksfas sharma@gmail.com khfdslk
fkjfsz
 kjnjvnfkdj iheoif j bfdkji b elow th eyyenlknklnl asjpovn@gmail.com hdifhidskj hciuashiu@hpoi.in knkdjf hihsdoin
iufdjankcns this is a text as a s string with emails are tanya2@redcliff.in akhjnfns
klshsjdh fiku@yahoo.com jkhfhf uihiuefh  start a day with this email kito@gmail.com 
jjfhs end the day with doip@kopi.com
"""

# check = re.compile(r'\b\s.*@')
# check = re.compile(r'.*@*\s$')
# check = re.compile(r'(\S*@*\S)@(\S*@*\S)')

check = re.compile(r'(\S*\S)@(\S*\S)')
matches = check.finditer(str)

# email=re.findall(r'((\S+\S)+@(\S+\S))',str)
email = re.findall(r'[0-9a-zA-Z._+%]+@[\w]+[.][0-9a-zA-Z]+',str)
print("This is findall email", email)
i = 1
# for match in matches:
#     print(f"This is Compile Email{i}:{match}")
#     i += 1