import src.url as http
from bs4 import BeautifulSoup


def get_image_source(soup_img):
    # return image source based on "src hierarchy"
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


def is_searched(soup_img, terms):
    # boolean check for "search tags" in a distinct image container
    # searches for matching-tags between image file names and alt attribute
    src = get_image_source(soup_img)
    alt = soup_img.get('alt')
    target = ' '.join(filter(None, [src, alt]))
    return any(word in target for word in terms)


def filter_links(soup_images, search_terms, url):
    # filtering based on "search tags"
    filtered_image = [
        img for img in soup_images if is_searched(img, search_terms)]

    # extracting links from filtered images
    img_links = []
    for img in filtered_image:
        src = get_image_source(img)
        if src:
            img_links.append(http.define_path(url, src))

    return img_links


def print_links(url, links):
    domain = http.get_domain(url)
    if links:
        print(f'\nImage links from {domain}')
        for link in links:
            print(link)
    else:
        print(f"\nNo Photos found on {domain}\n")


def parse_links(url, search_terms):
    # create soup container
    page_content = http.parse_content(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    images = soup.findAll('img')

    # extracting links from images based on "search tags"
    links = filter_links(images, search_terms, url)
    return links
