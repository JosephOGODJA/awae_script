# We import requests module to handle requests
import requests

# We import colorama to display results in different color
from colorama import Fore, Back, Style

# We disable certificate warning from websites with insecure certificate
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def format_text(title, item):
	cr = '\r\n'
	section_break = cr + "*" * 20 + cr
	item = str(item)
	text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
	return text

r = requests.get('https://access.redhat.com/errata/RHBA-2023:06601', verify=False)

print(format_text('r.status_code is: ', r.status_code))
print(format_text('r.header is: ', r.headers))

print(format_text('r.cookies is: ', r.cookies))
# print(format_text('r.text is: ', r.text))
