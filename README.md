# **Test Crawl Ảnh với Python, Beautiful Soup 4**

## Tìm hiểu Beautiful Soup 4

  Beautifulsoup 4 là một thư viện Python được sử dụng để phân tích cú pháp HTML và XML, giúp cho việc trích xuất thông tin từ các trang web trở nên dễ dàng hơn. Thư viện này cung cấp các công cụ để điều hướng, tìm kiếm và trích xuất dữ liệu từ cấu trúc HTML hoặc XML.

  Để sử dụng thì ta phải cài đặt thư viện này. Hãy gõ lệnh này vào Terminal
  > **pip install beautifulsoup4**
  
  Tôi sẽ dùng thư viện này để tải ảnh trên web https://this-person-does-not-exist.com/ về máy, cụ thể là vào file CrawlPic trong project này.
  ![image](https://github.com/HungHyperX/TestCrawlPicture/assets/131465286/40f0dccb-ab42-4ceb-aa07-12a58a6d65bb)

## Về trang web https://this-person-does-not-exist.com/

  Đây là trang web mà tôi sẽ test việc tải ảnh về.

  Đặc điểm của ảnh tải về là sau mỗi lần chạy project thì ảnh được tải về là ảnh một người được tạo ra tự động, đa dạng đặc điểm, không trùng nhau, và đặc biệt là không hề tồn tại ngoài đời thật nên không cần lo việc sử dụng hình ảnh mà không được phép

## Source code:

```py
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
```
Phạm Lưu Minh Hùng - 20215586


