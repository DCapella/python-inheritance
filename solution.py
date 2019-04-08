#########################
# !!! SOLUTION CODE !!! #
#########################

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
      self.firstName = firstName
      self.lastName = lastName
      self.idNumber = idNumber
      self.scores = scores
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
      avg = sum(self.scores) / len(self.scores)
      if avg < 40:
        grade = 'T'
      elif avg < 55:
        grade = 'D'
      elif avg < 70:
        grade = 'P'
      elif avg < 80:
        grade = 'A'
      elif avg < 90:
        grade = 'E'
      else:
        grade = 'O'
      return grade


line = input().split()
