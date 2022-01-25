# Python Program to depict multiple inheritance
# when method is overridden in one of the classes

class Class1:

	def m(self, input: str) -> None:
		if input == 'vishal':
			raise Exception
		a = 10 + 10
		print(a)

class Class2(Class1):
	pass

class Class3(Class1):
	def m(self):
		print("In Class3")
	
class Class4(Class2, Class3):
	pass	


obj = Class1()
obj.m('vishal')