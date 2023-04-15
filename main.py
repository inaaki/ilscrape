from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen, Request
import sys


def get_image_source(soup_img):
    # return image source based on src hierarchy
    try:
        src = soup_img['data-srcset']
    except:
        try:
            src = soup_img['data-src']
        except:
            try:
                src = soup_img['data-fallback-src']
            except:
                try:
                    src = soup_img['src']
                except:
                    src = ''
    return src


def is_searched(soup_img, terms) -> bool:
    # boolean check for "search tags" in a distinct image container
    src = get_image_source(soup_img)
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
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    req = Request(url, headers=headers)
    with urlopen(req) as page:
        page_content = page.read().decode('utf-8')

    # create soup container
    soup = BeautifulSoup(page_content, 'html.parser')
    images = soup.findAll('img')

    # filtering based on "search tags"
    filtered_image = [img for img in images if is_searched(img, search_terms)]

    # extracting links from filtered images
    img_links = [define_path(url, get_image_source(img))
                 for img in filtered_image if img.get('src')]

    if img_links:
        print(f'\nPhotos from {url}')
        for link in img_links:
            print(link)
    else:
        print(f"\nNo Photos found on {url}\n")


for url in URLs:
    print_image_links(url, SEARCH_TAGS)
