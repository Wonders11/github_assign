class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display(self):
        print(f'Firstname is {self.firstname} and lastname is {self.lastname}')

class Car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def display(self):
        print(f'Mohit has car named {self.model} from {self.brand}')

if __name__ == "__main__":
    person = Person("Mohit","Hedaoo")
    person.display()

    car = Car("X7","BMW")
    car.display()