from urllib.request import urlopen
from bs4 import BeautifulSoup


def is_searched(soup_img, terms) -> bool:
    # boolean check for "search tags" in a distinct image container
    src = soup_img.get('src')
    alt = soup_img.get('alt')
    target = ' '.join(filter(None, [src, alt]))
    return any(word in target for word in terms)


search_tags = ['coffee', 'blue', 'sky', 'flower', 'computer', 'table']
url = 'https://unsplash.com/'

with urlopen(url) as page:
    page_content = page.read()

# create soup container
soup = BeautifulSoup(page_content, 'html.parser')
images = soup.findAll('img')

# images that contain any word of "search tags"
filtered_image = [img for img in images if is_searched(img, search_tags)]

# extracting links from filtered images
img_links = [img.get('src') for img in filtered_image if img.get('src')]

for link in img_links:
    print(link)
