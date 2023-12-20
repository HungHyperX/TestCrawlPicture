import os
import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

# Chọn URL trang cần tải ảnh về
pageTarget = 'https://this-person-does-not-exist.com/'
page = requests.get(pageTarget)

# Phân tích HTML bằng Beautiful Soup 4
soup = BeautifulSoup(page.content, 'html.parser')

# Tìm thẻ <body>
wrapper = soup.find('body')

# Tìm tất cả có thẻ <img id: "avatar">
images = wrapper.find_all("img", {'id': 'avatar'})

for image in images:
  imgData = image['src']
  print(imgData) # In tên ảnh tải về
  if("data:image" not in imgData):
    if(imgData):

      filename = imgData.split('/')[-1] # Tách đường dẫn src để lấy phần ảnh

      picSrc = f"{pageTarget}/{imgData}"
      response = requests.get(picSrc)

      img_path = os.path.join("CrawlPic", filename)

      file = open(img_path, "wb")
      file.write(response.content)

      file.close()