from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

'''整体思路为：构造文档对象，解析文档对象，提取所需内容'''


def parse():
    fn = open('C:\\Users\\Administrator\\Desktop\\保单贷\\保单质押贷款合同.pdf', 'rb')
    # 创建一个pdf文档分析器
    parser = PDFParser(fn)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码 doc.initialize("foo")
    # 如果没有密码，创建一个空字符串
    doc.initialize("")
    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建pdf资源管理器
        resource = PDFResourceManager()
        # 创建一个PDF参数分析器
        laparams = LAParams()
        # 创建聚合器，用于读取文档的对象
        device = PDFPageAggregator(resource, laparams=laparams)
        # 创建解释器，对文档编码，解释成 python 能识别的格式
        interpreter = PDFPageInterpreter(resource, device)
        # 循环遍历列表，每次处理一页内容
        # doc.get_pages() # 获取page列表
        for page in doc.get_pages():
            # 使用解释器的 process_page() 方法解析读取单独页数
            interpreter.process_page(page)
            # 使用聚合器 get_result() 方法获取内容
            layout = device.get_result()
            # layout 是一个 LTPage 对象，存放着page 解析出的各种对象
            for out in layout:
                # 判断是否含有 get_text() 方法
                if hasattr(out, "get_text"):
                    print(out.get_text())
                    with open('text.txt', 'a', encoding='utf8') as f:
                        f.write(out.get_text() + '\n')


def main():
    parse()


if __name__ == '__main__':
    main()
