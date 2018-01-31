# 该脚本通过单线程进行下载图书排名信息的调用
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib import request

REGEX = compile('#([\d,]+) in Books')
AMZN = 'https://www.amazon.com/'
ISBNs = {
    '013': 'Core Python Programming'
}
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()


def getRanking(isbn):
    page = request.urlopen('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print('_ %r ranked %s' % (ISBNs[isbn], getRanking(isbn)))


def _main():
    print('at', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        _showRanking(isbn)


@register
def _atexit():
    print('all done at:', ctime())


if __name__ == '__main__':
    _main()