from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen
import sys


def is_searched(soup_img, terms) -> bool:
    # boolean check for "search tags" in a distinct image container
    src = soup_img.get('src')
    alt = soup_img.get('alt')
    target = ' '.join(filter(None, [src, alt]))
    return any(word in target for word in terms)


def define_path(url, link):
    # convert relative path to an absolute one
    if link and urlparse(link).netloc:
        return link
    return urljoin(url, link)


URLs = sys.argv[1]
SEARCH_TAGS = sys.argv[2]
URLs = URLs.split()
SEARCH_TAGS = SEARCH_TAGS.split()



def print_image_links(url, search_terms):

    with urlopen(url) as page:
        page_content = page.read()

    # create soup container
    soup = BeautifulSoup(page_content, 'html.parser')
    images = soup.findAll('img')

    # filtering based on "search tags"
    filtered_image = [img for img in images if is_searched(img, search_terms)]

    # extracting links from filtered images
    img_links = [define_path(url, img.get('src'))
                 for img in filtered_image if img.get('src')]

    if img_links:
        print(f'\nPhotos from {url}')
        for link in img_links:
            print(link)
    else:
        print(f"\nNo Photos found on {url}\n")


for url in URLs:
    print_image_links(url, SEARCH_TAGS)
