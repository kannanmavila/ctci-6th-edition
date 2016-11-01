"""Q: An animal shelter, which holds only dogs and cats, operate on
strictly "first in, first out" basis. People must adopt either the
"oldest" (based on arrival time) of all animals at the shelter, or
they can select whether they would prefer a dog or cat (and will
receive the oldest animal of that type). They cannot select which
specific animal they would like. Create the data structure to
maintain this system and implement operations such as enqueue,
dequeue_any, dequeue_cat and dequeue_dog. You may use the built-in
LinkedList data structure"""

from copy import deepcopy


class UnknownAnimal(ValueError):
	"""Shelter supports only cats and dogs."""
	pass


class EmptyShelter(IndexError):
	"""Animal not present."""
	pass


class Animal(object):
	"""A cat or a dog."""
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.next = None
		self.prev = None
		self.next_typed = None

	def __str__(self):
		return self.type.upper() + ":" + self.name

	def __repr__(self):
		return str(self)


class Cat(Animal):
	"""Meow."""
	def __init__(self, name):
		Animal.__init__(self, name, "cat")


class Dog(Animal):
	"""Woof woof."""
	def __init__(self, name):
		Animal.__init__(self, name, "dog")


class Shelter(object):
	"""An animal shelter adoption queue."""
	def __init__(self):
		# Pointers to track the youngest and oldest
		# of cats, dogs, and animals in general.
		self.oldest_cat = self.youngest_cat = None
		self.oldest_dog = self.youngest_dog = None
		self.oldest = self.youngest = None

	def _oldest(self, type=None):
		if type is None: return self.oldest
		if type == "cat": return self.oldest_cat
		if type == "dog": return self.oldest_dog

	def _update_oldest(self, type):
		if self.oldest == self._oldest(type):
			self.oldest = self.oldest.next

		if type == "cat":
			self.oldest_cat = self.oldest_cat.next_typed
		elif type == "dog":
			self.oldest_dog = self.oldest_dog.next_typed

	def _youngest(self, type):
		if type == "cat": return self.youngest_cat
		if type == "dog": return self.youngest_dog

	def _update_youngest(self, animal):
		self.youngest = animal

		if animal.type == "cat":
			self.youngest_cat = animal
		elif animal.type == "dog":
			self.youngest_dog = animal

	def enqueue(self, animal):
		if animal is None:
			raise ValueError('Animal cannot be None')
		if not animal.type in ("cat", "dog"):
			raise ValueError('Unknown animal')

		def _first_of_a_kind():
			"""The first cat/dog."""
			if animal.type == "cat" and self.oldest_cat is None:
				self.oldest_cat = self.youngest_cat = animal
			elif animal.type == "dog" and self.oldest_dog is None:
				self.oldest_dog = self.youngest_dog = animal

		# First animal
		if self.empty():
			self.oldest = self.youngest = animal
			_first_of_a_kind()
			return

		try:
			self._youngest(animal.type).next_typed = animal
		except AttributeError:
			_first_of_a_kind()
		self.youngest.next = animal
		animal.prev = self.youngest
		self._update_youngest(animal)

	def dequeue(self, type=None):
		if not type in (None, "cat", "dog"):
			raise ValueError('Unknown animal')

		animal = self._oldest(type)
		if animal is None:
			raise EmptyShelter('Animal not present')

		# Identify the new seniors in all categories
		self._update_oldest(animal.type)

		# Patch up the overall age links
		# a. Forwards
		try:
			animal.prev.next = animal.next
		except AttributeError:
			pass
		# b. Backwards
		try:
			animal.next.prev = animal.prev
		except AttributeError:
			pass

		return animal

	def empty(self):
		return self.oldest is None


if __name__ == "__main__":
	c1 = Cat('1')
	c2 = Cat('2')
	c3 = Cat('3')
	c4 = Cat('4')
	d1 = Dog('1')
	d2 = Dog('2')
	d3 = Dog('3')
	shelter_ = Shelter()
	for a in [c1, c2, d1, c3, d2]:
		print "queueing:", a
		shelter_.enqueue(a)

	print "--order--"
	shelter = deepcopy(shelter_)
	old = shelter.oldest
	while old is not None:
		print old
		old = old.next

	print "--dequeueing--"
	while not shelter.empty():
		print shelter.dequeue()

	print "-- C D C D C --"
	c, d = "cat", "dog"
	shelter = deepcopy(shelter_)
	for type in [c, d, c, d, c]:
		print shelter.dequeue(type)

	print "-- D C C C D --"
	shelter = deepcopy(shelter_)
	for type in [d, c, c, c, d]:
		print shelter.dequeue(type)

	print "-- D C C --"
	shelter = deepcopy(shelter_)
	for type in [d, c, c]:
		print shelter.dequeue(type)
	for a in [c4, d3]:
		shelter.enqueue(a)
	print "--dequeueing--"
	while not shelter.empty():
		print shelter.dequeue()
