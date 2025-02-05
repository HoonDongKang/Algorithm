class Person:
  def __init__(self, name_param):
    self.name = name_param
    print("hihi I am created", self)

  def talk(self):
    print("Hi, my name is", self.name)

person_1 = Person("Tom")
person_1.talk()
person_2 = Person("Danniel")
