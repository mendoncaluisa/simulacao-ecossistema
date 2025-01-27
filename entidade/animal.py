class animal:
    def __init__(self, id, alimentary, type, stamina, age):
        self.id = id
        self.alimentary = alimentary
        self.type = type
        self.stamina = stamina
        self.age = age


    def eat(self, alimento, animal):
        animal.stamina = alimento.stamina
        return animal


    def age_incrementer(self, animal):
        animal.age += 1
        if animal.age >= 10:
            self.die(animal)

    def stamina_decrementer(self, animal):
        animal.stamina -= 1
        if animal.stamina == 0:
            self.die(animal)

    def die(self, animal):
        return

    def born(self):
        return