import src.args as args
import src.imglib as img


def main():
    (urls, search_tags) = args.args_parse()
    for url in urls:
        links = img.parse_links(url, search_tags)
        img.print_links(url, links)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nYou have exited the program... Bye :(\n')
