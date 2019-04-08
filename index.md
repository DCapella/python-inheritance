# Python Inheritance

#### [HackerRank](www.hackerrank.com)

> Complete the Student class by writing the following:
> A Student class constructor, which has  parameters:
> A string, firstName.
> A string, lastName.
> An integer, id.
> An integer array (or vector) of test scores, scores.
> A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average.

This one is basically a given so there's no real process here. At least it's interesting though.

## Code

### Class constructor

```python
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
```

### Char calculate method

```python
...
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
```

### Full Code

```python
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
```

## Conclusion

Well, not the most exciting one but still a good warm up.
