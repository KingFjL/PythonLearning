'''
使用collections模块中的OrderedDict实现FIFO(先进先出)的dict，
当容量超出限制时，先删除最早添加的key.
'''

from collections import OrderedDict


class LastUpdatedOrederedDict(OrderedDict):

	def __init__(self, capacity):
		super(LastUpdatedOrederedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print 'remove:', last
		if containsKey:
			del self[key]
			print 'set:', (key, value)
		else:
			print 'add:', (key, value)
		OrderedDict.__setitem__(self, key, value)
