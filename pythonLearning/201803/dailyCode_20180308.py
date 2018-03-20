"""
realoadall.py: transitively reload nested modules
通用的全导入工具
"""


import types
from imp import reload


def status(module):
    print('reloading ' + module.__name__)


def transitive_reload(module: types.ModuleType, visited):
    if module not in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attr in module.__dict__.values():
            if type(attr) == types.ModuleType:
                transitive_reload(attr, visited)


def reload_all(*args):
    print('reload_all')
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


def main():
    import dailyCode_20180308
    reload_all(dailyCode_20180308)


if __name__ == '__main__':
    main()
