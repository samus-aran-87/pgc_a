class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def get_name(self):
		return self.name

	def bark(self):
		print("bark")

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age


#############################


class Student:

	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade


class Course:
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []
		# self.is_active = True

	def add_student(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)


# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 18, 75)
# s3 = Student("Jill", 20, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)

# print(course.add_student(s3))
# print(course.get_average_grade())


#############################


class Pets:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("I don't know what I say")


class Cats(Pets):

	# def __init__(self, name, age):
	# 	self.name = name
	# 	self.age = age

	def speak(self):
		print("Meow")


class Dogs(Pets):

	# def __init__(self, name, age):
	# 	self.name = name
	# 	self.age = age

	def __init__(self, name, age, color):
		# self.name = name
		# self.age = age
		super().__init__(name, age)
		self.color = color

	def speak(self):
		print("Bark")

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Fish(Pets):
	pass


# p = Pets("Tim", 19)
# p.show()
# p.speak()
# print()


# c = Cats("Bill", 18)
# c.show()
# c.speak()
# print()

# d = Dogs("Jill", 25, "Green")
# d.show()
# d.speak()
# print()

# d = Fish("Tod", 35)
# d.show()
# d.speak()
# print()


#############################


class Person:
	number_of_people = 0
	GRAVITY = -9.8

	def __init__(self, name):
		self.name = name
		# Person.number_of_people += 1
		Person.add_person()

	@classmethod
	def number_of_people_(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1


p1 = Person("Tim")
# print(Person.number_of_people)
# print(p1.number_of_people)

p2 = Person("Jill")
# print(Person.number_of_people)
# print(p2.number_of_people)

# print(Person.number_of_people_())


#############################


class Math:

	@staticmethod
	def add5(x):
		return x + 5

	@staticmethod
	def add10(x):
		return x + 10

	@staticmethod
	def pr():
		print("run")


# m = Math()
print(Math.add5(5))
print(Math.add10(5))
Math.pr()









