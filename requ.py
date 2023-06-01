import requests
from bs4 import BeautifulSoup
url = 'http://data.gov'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
#1
titles = soup.find_all('title')
for title in titles:
    print(title.text)
print('--------------------------')
#2
ps = soup.find_all('p')
for p in ps:
    print(p.text)
print('--------------------------')
#3
print(len(ps))
print('--------------------------')
#4
first = soup.find('p')
print(first)
print('--------------------------')
#5
h2_tag = soup.find('h2')

if h2_tag:
    text_length = len(h2_tag.text)
    print("Довжина тексту першого тегу <h2>: ", text_length)
else:
    print("Тег <h2> не знайдено.")
#6
print('--------------------------')
a = soup.find('a')
print("Текст першого тегу <a>: ", a)
#7
print('--------------------------')
hr = a['href']
print(hr)
#8
print('--------------------------')
url1 = 'https://mof.gov.ua/uk'
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.text, 'lxml')
li_tags = soup1.find_all('li')
urls = [li.a['href'] for li in li_tags if li.a]
print(urls)
print('--------------------------')
#9
h2_teg = soup1.find_all('h2')
first_four_h2 = [h2.text for h2 in h2_teg[:4]]
print(first_four_h2)
print('--------------------------')
#10
a_tags = soup1.find_all('a')
first_ten_a = [a['href'] for a in a_tags[:10]]
print(first_ten_a)
print('--------------------------')
#11
h1_tags = soup1.find_all('h1')
h2_tags = soup1.find_all('h2')
h3_tags = soup1.find_all('h3')
print(h1_tags + h2_tags + h3_tags)
print('--------------------------')
#12
txt1 = soup1.get_text()
print(txt1)
print('--------------------------')
#13
tags = soup1.find_all()
# Виводимо імена тегів
ls = []
for tag in tags:
    ls.append(tag.name)
print(ls)
print('--------------------------')
#14
parent_tag = 'html'
parent_element = soup1.find(parent_tag)
nested_tags = parent_element.find_all()
lss = []
for x in nested_tags:
    lss.append(x.name)
print(lss)
print('--------------------------')
#15
tag_body = soup1.find('body')
desc = tag_body.descendants
ls1 = []
for y in desc:
    ls1.append(y.name)
print(ls1)
print('--------------------------')
#16
h1_tag = soup1.find('h1')
h1_html = str(h1_tag)
h1_text = h1_tag.get_text()
parent_html = str(h1_tag.parent)  
print(h1_html)  
print(h1_text)
print(parent_html)
print('--------------------------')
#17
li_tag = soup1.find_all('li')
for li in li_tag:
    print(li.get_text())
print('--------------------------')
#18
search_string = '10'
elements = soup1.find_all(string=lambda text: search_string in text)
for element in elements:
    print(element.strip())
print('--------------------------')
#19
element_id = 'content-wrapper'
elements = soup1.find_all(id=element_id)
for element in elements:
    print(element)
print('--------------------------')
#20
attribute_name = 'href'  
attribute_value = '100'
tag = soup1.find(lambda t: t.has_attr(attribute_name) and t[attribute_name] == attribute_value)
print(tag)
print('--------------------------')
#21
parent_tag = 'div'
nested_tags = soup1.find_all(parent_tag)
for tag in nested_tags:
    print(tag)
print('--------------------------')
#22
class_name = 'class'
tags = soup.find_all(class_=class_name)
for tag in tags:
    print(tag)
print('--------------------------')
#23
tag_to_modify = 'h1'
new_content = 'New Heading'
tag = soup1.find(tag_to_modify)
if tag:
    tag.string = new_content
    print(f"Змінений вміст тегу <{tag.name}>: {tag.string}")
else:
    print(f"Тег <{tag_to_modify}> не знайдено.")
updated_html = soup1.prettify()
print('--------------------------')
#24
tag_to_modify = 'p'  
new_content = 'Additional content'
tag = soup1.find(tag_to_modify)
if tag:
    new_element = soup1.new_string(new_content)
    tag.append(new_element)
    print(f"Вміст додано до тегу <{tag.name}>.")
else:
    print(f"Тег <{tag_to_modify}> не знайдено.")
updated_html = soup1.prettify()
print('--------------------------')
#25
new_text = '/smth'
current_text = soup1.get_text()
new_url_text = url.replace(current_text, current_text + new_text)
print(new_url_text)
