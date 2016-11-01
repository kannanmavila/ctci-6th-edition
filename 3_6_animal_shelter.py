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
from datetime import datetime


class UnknownAnimal(ValueError):
	"""Shelter supports only cats and dogs."""
	pass


class EmptyShelter(IndexError):
	"""Animal not present."""
	pass


class ShelterAnimal(object):
	"""A cat or a dog."""
	def __init__(self, name, type):
		self.name = name
		self.type = type

	def __str__(self):
		return self.type.upper() + ":" + self.name

	def __repr__(self):
		return str(self)


class Cat(ShelterAnimal):
	"""Meow."""
	def __init__(self, name):
		ShelterAnimal.__init__(self, name, "cat")


class Dog(ShelterAnimal):
	"""Woof woof."""
	def __init__(self, name):
		ShelterAnimal.__init__(self, name, "dog")


class Shelter(object):
	"""An animal shelter adoption queue."""
	def __init__(self):
		self.cats = []
		self.dogs = []

	def _dog(self):
		return self.dogs.pop(0)[1]

	def _cat(self):
		return self.cats.pop(0)[1]

	def enqueue(self, animal):
		if animal is None:
			raise ValueError('Animal cannot be None')

		if animal.type == "cat":
			self.cats.append((datetime.now(), animal))
		elif animal.type == "dog":
			self.dogs.append((datetime.now(), animal))
		else:
			raise ValueError('Unknown animal')

	def dequeue(self, type=None):
		# Wants a cat
		if type == "cat":
			try:
				return self._cat()
			except IndexError:
				raise EmptyShelter('No cats')

		# Wants a dog
		if type == "dog":
			try:
				return self._dog()
			except IndexError:
				raise EmptyShelter('No dogs')

		# Wants just any animal
		if type is None:
			if self.empty():
				raise EmptyShelter('No animals')

			if not self.cats: return self._dog()
			if not self.dogs: return self._cat()
			if self.cats[0] < self.dogs[0]:
				return self._cat()
			return self._dog()

		raise ValueError('Unknown animal')

	def empty(self):
		return not (self.cats or self.dogs)


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

	print "--dequeueing--"
	shelter = deepcopy(shelter_)
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
	for a in [d3, c4]:
		shelter.enqueue(a)
	print "--dequeueing--"
	while not shelter.empty():
		print shelter.dequeue()
