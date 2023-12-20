import requests
from bs4 import BeautifulSoup

pageTarget = 'https://this-person-does-not-exist.com/'
page = requests.get(pageTarget)
soup = BeautifulSoup(page.content, 'html.parser')
wrapper = soup.find('body')

images = wrapper.find_all("img", {'id': 'avatar'})

for image in images:
  imgData = image['src']
  print(imgData)
  if("data:image" not in imgData):
    if(imgData):

      filename = imgData.split('/')[-1]

      picSrc = f"{pageTarget}/{imgData}"
      response = requests.get(picSrc)

      file = open(filename, "wb")
      file.write(response.content)
      file.close()