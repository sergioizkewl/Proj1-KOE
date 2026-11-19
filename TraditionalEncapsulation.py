class Student:
  def __init__(self, name, grade):
    self.__name=name
    self.__grade=grade

  #GETTER
  def get_grade(self):
    return self.__grade

  #SETTER
  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade=grade
    else:
      print("Invalid Grade!")

#main code
student1=Student("Leslie", 95)
student1.set_grade(105)

#access the private attribute using getter method
student1.get_grade()

print(student1.get_grade())