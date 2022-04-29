import re

text = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North suresh@gmail.com America
1700 North js99@codewithharry.com Moore St, Suite 1520
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
Directions: View tarun@gmail.com map fass
harry bhai lekin
Email: north@uk.co.in
bahut hi badia aadmi ldk@fdsf haiaiinaiiiiiiiiiiii
'''

path = re.compile(r'\w+@\S+.com')
email = re.findall(r"[a-z0-9._+%]+@[a-z0-9A-Z._+%]+[.][a-z0-9A-Z.0-9]+", text)
# matches = path.findall(text)
for em in email:
    with open("tar_email.txt","a") as f:
        f.write(em + "\n")
print(text[427: 428])
