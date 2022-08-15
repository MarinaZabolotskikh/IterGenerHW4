class FlatIterator:

	def __init__(self, nested_list):
		self.nested_list = nested_list

	def __iter__(self):
		self.cursor = 0
		self.inner = -1
		return self

	def __next__(self):
		self.inner += 1
		if self.inner >= len(self.nested_list[self.cursor]):
			self.cursor += 1
			self.inner = 0
		if self.cursor >= len(self.nested_list):
			raise StopIteration
		return self.nested_list[self.cursor][self.inner]

class FlatIteratorComplex:

	def __init__(self, nested_list):
		self.nested_list = nested_list

	def __iter__(self):
		self.temporary_list = []
		self.iterator = iter(self.nested_list)
		return self

	def __next__(self):
		while True:
			try:
				self.element = next(self.iterator)
			except StopIteration:
				if not self.temporary_list:
					raise StopIteration
				else:
					self.iterator = self.temporary_list.pop()
					continue
			if isinstance(self.element, list):
				self.temporary_list.append(self.iterator)
				self.iterator = iter(self.element)
			else:
				return self.element

def flat_generator(list_):
	for list_of_lists in list_:
		for item in list_of_lists:
			yield item

def flat_generator_complex(list_):
    for elem in list_:
        if isinstance(elem, list):
            for el in flat_generator_complex(elem):
                yield el
        else:
            yield elem

if __name__ == '__main__':

	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f'],
		[1, 2, None],
	]

	nested_list2 = [
		['a'], ['b'], ['c'],
		[1,2,3,4], ['d', [5],
		['e'], [6, 7, [8]]]
	]

	print("-------------Iterators------------")
	for item in FlatIterator(nested_list):
		print(item)

	print("-------------Comprehension------------")
	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)

	print("-------------Generators------------")
	for item in flat_generator(nested_list):
		print(item)

	print("-------------Iterators2------------")
	for el in FlatIteratorComplex(nested_list2):
		print(el)

	print("-------------Generators2------------")
	for el in flat_generator_complex(nested_list2):
		print(el)