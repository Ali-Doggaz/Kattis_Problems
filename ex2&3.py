import random


class Person:
    def __init__(self, Name, Age, Height, Salary):
        self.Name = Name
        self.Age = Age
        self.Height = Height
        self.Salary = Salary

    def Birthday(self):
        self.Age += 1

    def Raise(self, x):
        # x is a float that corresponds to the raise percentage. Example values: 10, 20, 32.5

        # We pick a random number between 1 and 100. There is a 1% chance of that number being 1.
        # If it is the case, we "fire" that employee. We set their salary to 0.
        if (random.randint(1, 100) == 1):
            self.Salary = 0
        else:
            self.Salary = self.Salary *(1 + (x/100))

    def __str__(self):
        return "Name: " + self.Name + " - Age: " + str(self.Age) + \
               " - Height: " + str(self.Height) + " - Salary: " + str(self.Salary)

if __name__ == '__main__':
   p1 = Person("Bob", 20, 6.0, 10000.0)
   p2 = Person("p2", 30, 180, 1000)
   p3 = Person("p3", 25, 6.0, 10000.0)
   p4 = Person("p4", 25, 180, 1000)
   p5 = Person("p4", 25, 180, 2000)
   p6 = Person("p4", 25, 170, 1000)

   print("p1 age is: " + str(p1.Age))
   p1.Birthday()
   print("p1 age is: " + str(p1.Age))

   print("p2 salary is: " + str(p2.Salary))
   p2.Raise(10)
   print("p2 salary is: " + str(p2.Salary))

   ListOfPersons = [p1, p2, p3, p4, p5, p6]
   sorted_list = sorted(ListOfPersons, key=lambda x: (-1*x.Age, x.Height, -1*x.Salary))

   for elem in sorted_list:
       print(elem)