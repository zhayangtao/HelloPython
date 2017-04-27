# python 类方法与静态方法
class a():
    @staticmethod
    def staticm():  # 静态方法
        print('static:')

    def normalm(self):  # 普通方法
        print('normal:', self)

    @classmethod  # 类方法
    def classm(cls):
        print('class:', cls)


a1 = a()
print(a1.normalm())
print(a1.staticm())
print(a1.classm())