#!/usr/bin/env python3

class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    pass


class Person(Human):
    def __init__(self, name, tax_number):
        self.name = name
        self.tax_number = tax_number

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, tax_number={self.tax_number!r})'


# TODO: fill classes above with the required logic
#       to represent human and person (probably with tax number, ...)
# TODO: try to make an Enterprise able to own Pets
# TODO: - add class to represent vaccine
#       - add class to represent generic chip,
#           and separate subclasses for concrete animal ID chips
#       - anything other you want to extend here


class Vaccine:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r})'


class GenericChip:
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(code={self.code!r})'


class AnimalIDChip(GenericChip):
    def __init__(self, code, manufacturer):
        super().__init__(code)
        self.manufacturer = manufacturer

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(code={self.code!r}, manufacturer={self.manufacturer!r})'


class Enterprise:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        pet.change_owner(self)

    def remove_pet(self, pet):
        self.pets.remove(pet)
        pet.change_owner(None)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(name={self.name!r}, owner={self.owner!r}, pets={self.pets!r})'


class Pet(Animal):
    """Abstracts an animal with an owner and name.

    Each pet is an animal having an owner and a name --
    that is how we model it.
    """

    def __init__(self, owner):
        """Set owner at instantiation."""
        self.change_owner(owner)
        self.vaccine = None
        self.chip = None

    def change_owner(self, new_owner):
        """Called to transfer ownership or set a new owner."""
        self.owner = new_owner

    @property
    def owner(self):
        """Dummy getter for hidden method."""
        return self.__owner

    @owner.setter
    def owner(self, value):
        """This is called when setting owner.

        The difference is that here we can check
        what the user sets owner to. E.g. check
        that owner is not number.

        Called at dog.owner = value
        """
        # do some checks here
        if isinstance(value, (Person, Enterprise)):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance'
            err += ' or subclass of Person.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(owner={self.owner!r}, vaccine={self.vaccine!r}, chip={self.chip!r})'


def main(args):
    person = Person(name='John Doe', tax_number='123456789')
    enterprise = Enterprise(name='ABC Inc.', owner=person)
    pet = Pet(owner=enterprise)

    vaccine = Vaccine(name='Good')
    pet.vaccine = vaccine

    chip = AnimalIDChip(code='ABCDE', manufacturer='Chip Company')
    pet.chip = chip

    enterprise.add_pet(pet)

    print(person)
    print(enterprise)
    print(pet)
    print(pet.vaccine)
    print(pet.chip)

if __name__ == '__main__':
    import sys

    main(sys.argv)

