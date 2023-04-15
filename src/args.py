import sys


def args_parse():
    # returns cli arguments as tuple
    URLs = sys.argv[1]
    SEARCH_TAGS = sys.argv[2]
    URLs = URLs.split()
    SEARCH_TAGS = SEARCH_TAGS.split()
    return URLs, SEARCH_TAGS
