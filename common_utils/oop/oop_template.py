class Animal(object):
    def __init__(self, name):
    	self._name = name
    def say(self, message):
    	print '%s the animal says %s' % (self._name, message)
    def get_number_of_legs(self):
    	raise NotImplementedError('get_number_of_legs')

class Cat(Animal):
    def __init__(self, name='Felix'):
    	Animal.__init__(self, name)
    def say(self, message):
    	print '%s the cat meows %s' % (self._name, message)
    def get_number_of_legs(self):
    	return 4

class Dog(Animal):
    def __init__(self, name='Fido'):
    	super(Dog, self).__init__(name)
    def say(self, message):
    	print '%s the dog barks %s' % (self._name, message)
    def get_number_of_legs(self):
    	return 4	

class Monkey(Animal):
    def __init__(self, name='George'):
    	Animal.__init__(self, name)
    def say(self, message):
    	print '%s the monkey sings %s' % (self._name, message)
    def get_number_of_legs(self):
    	return 2

class CatDog(Cat, Dog):
	pass




animal = Animal('Generic')
animal.say('hey')
# animal.get_number_of_legs()

cat = Cat()
cat.say('hey hey hey')
cat_legs = cat.get_number_of_legs()
print cat_legs

monkey = Monkey()
monkey.say('I have %s legs' % monkey.get_number_of_legs())

dog = Dog()
dog.say('delion')

print isinstance(dog, Dog)
print isinstance(dog, Cat)
print isinstance(dog, Animal)
print issubclass(Dog, Animal)
print issubclass(Dog, Monkey)

x = CatDog('What is this?!')
print x.say('hello?')

print CatDog.mro()