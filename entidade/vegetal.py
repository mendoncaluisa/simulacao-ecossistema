class vegetal:
    def __init__(self, id, alimentary, type, stamina, age):
        self.id = id
        self.alimentary = alimentary
        self.type = type
        self.stamina = stamina
        self.age = age


    def eat(self, alimemnto, vegetal):
        vegetal.stamina = alimemnto.stamina
        return vegetal


    def age_incrementer(self, vegetal):
        vegetal.age += 1
        if vegetal.age >= 10:
            self.die(vegetal)

    def stamina_decrementer(self, vegetal):
        vegetal.stamina -= 1
        if vegetal.stamina == 0:
            self.die(vegetal)

    def die(self, vegetal):
        return

    def born(self):
        return