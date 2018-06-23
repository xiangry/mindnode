#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


class AtleteList(list):
    def __init__(self, name, dob=None, times = []):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self])))[0:3]



'''
DEMO: 示例
    vera = AtleteList("veravi")
    vera.append("1.31")
    print(vera.top3())
    vera.extend(['2.22', '1-21', '2.22'])
    print(vera.top3())
'''