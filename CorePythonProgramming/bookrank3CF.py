# 使用了 concuttent.futures 模块的图书排名 screenscraper
from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen as uopen


REGEX = compile(b'#([\d,]+) in Books')
AMZN = "http://www.baidu.com"
ISBNs = {
    '123'
}


def getRanking(isbn):
    with uopen('{0}{1}'.format(AMZN, isbn)) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')


def _main():
    print('At', ctime(), 'on baidu...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNs, executor.map(getRanking, ISBNs)):
            print('- %r ranked %s' % (ISBNs[isbn], ranking))
    print('all done at:', ctime())


if __name__ == '__main__':
    _main()