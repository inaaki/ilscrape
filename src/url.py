from urllib.parse import urlparse, urljoin
from urllib.request import urlopen, Request


def get_domain(url):
    return urlparse(url).netloc


def define_path(url, link):
    # convert relative path to an absolute one
    if link and get_domain(link):
        return link
    return urljoin(url, link)


def parse_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    req = Request(url, headers=headers)
    with urlopen(req, timeout=10) as page:
        page_content = page.read().decode('utf-8')
    return page_content
