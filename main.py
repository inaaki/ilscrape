from urllib.request import urlopen
from bs4 import BeautifulSoup


def is_searched(soup_img, terms) -> bool:
    # boolean check for "search tags" in a distinct image container
    src = soup_img.get('src')
    alt = soup_img.get('alt')
    target = ' '.join(filter(None, [src, alt]))
    return any(word in target for word in terms)


SEARCH_TAGS = ['coffee', 'blue', 'sky', 'flower', 'computer', 'table']
URLS = ['https://unsplash.com/', 'https://www.shutterstock.com/images']


def print_image_links(url, search_terms):

    with urlopen(url) as page:
        page_content = page.read()

    # create soup container
    soup = BeautifulSoup(page_content, 'html.parser')
    images = soup.findAll('img')

    # filtering based on "search tags"
    filtered_image = [img for img in images if is_searched(img, search_terms)]

    # extracting links from filtered images
    img_links = [img.get('src') for img in filtered_image if img.get('src')]

    if img_links:
        for link in img_links:
            print(f'\nPhotos from {url}')
            print(link)
    else:
        print(f"\nNo Photos found on {url}\n")


for url in URLS:
    print_image_links(url, SEARCH_TAGS)
