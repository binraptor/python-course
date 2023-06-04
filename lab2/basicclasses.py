#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def __repr__(self):
        return f"""Person:
    Name: {self.name}
    Age: {self.age}\n"""


class Worker(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def __repr__(self):
        return f"""Worker:
    Name: {self.name}
    Age: {self.age}
    Company: {self.company.name}\n"""


class Company:
    def __init__(self, name, workers):
        self.name = name
        self.workers = workers

    def hire_worker(self, worker):
        self.workers.append(worker)

    def __repr__(self):
        return f"""Company:
    Name: {self.name}
    Workers:\n{self.workers}\n"""

def main(args):
    
    person1 = Person("John", 26)
    person1.greet()
    print(person1)

    company1 = Company("ABC Inc.", [])

    worker1 = Worker("Alice", 21, company1)
    worker2 = Worker("Bob", 27, company1)
    company1.hire_worker(worker1)
    company1.hire_worker(worker2)

    print(company1)
    print(worker1)
    print(worker2)

if __name__ == '__main__':
    import sys

    main(sys.argv)

