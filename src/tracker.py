import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.myntra.com/2211670'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

block = soup.findAll('script', {'type': 'application/ld+json'})[1]

final_myntra_json_stats = json.loads(block.text.strip())

print(final_myntra_json_stats['name'])

print(final_myntra_json_stats['offers']['price'])

print(final_myntra_json_stats['brand']['name'])

# scripts = soup.find_all('script')
#
# tag = ''
# for script in soup(text=re.compile(r'__myx_seo__' )):
#     tag = script.parent.text
#     break
#
# meta_string = tag.split('=')[1]
# # spilt on \n to get only first tag
# meta_json_string = meta_string.split('\n')[0]
# # get rid of ; at the end
# meta_json_string = meta_json_string.split(';')[0]
# # get the json from the string available
# final_myntra_json = json.loads(meta_json_string.strip())
#
# print(final_myntra_json['metaData']['description'].split('Rs. ')[1][0:4])
