import random
import matplotlib.pyplot as plt

class Person:
    def __init__(self, age):
        self.gender = random.randint(0, 1)
        self.age = age
        self.pregnant = 0

class PopulationSimulator:
    def __init__(self, start_population, infant_mortality, youth_mortality, agriculture, disaster_chance, fertilityx, fertilityy):
        self.start_population = start_population
        self.infant_mortality = infant_mortality
        self.youth_mortality = youth_mortality
        self.agriculture = agriculture
        self.disaster_chance = disaster_chance
        self.fertilityx = fertilityx
        self.fertilityy = fertilityy
        self.food = 0
        self.people = []

    def harvest(self):
        able_people = sum(1 for person in self.people if person.age > 8)
        self.food += able_people * self.agriculture

        if self.food < len(self.people):
            del self.people[0:int(len(self.people) - self.food)]
            self.food = 0
        else:
            self.food -= len(self.people)

    def reproduce(self):
        for person in self.people:
            if person.gender == 1 and self.fertilityx < person.age < self.fertilityy and random.randint(0, 5) == 1:
                if random.randint(0, 100) > self.infant_mortality:
                    self.people.append(Person(0))

    def begin_simulation(self):
        for _ in range(self.start_population):
            self.people.append(Person(random.randint(18, 50)))

    def run_year(self):
        self.harvest()

        to_remove = []
        for person in self.people:
            if person.age > 80:
                to_remove.append(person)
            else:
                person.age += 1

        for person in to_remove:
            self.people.remove(person)

        self.reproduce()

        if random.randint(0, 100) < self.disaster_chance:
            to_remove = self.people[0:int(random.uniform(0.05, 0.2) * len(self.people))]
            for person in to_remove:
                self.people.remove(person)

        return len(self.people)

    def simulate(self):
        years = []
        population = []

        self.begin_simulation()

        while 1 < len(self.people) < 250:
            population.append(self.run_year())
            years.append(len(years) + 1)

        plt.plot(years, population)
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.title('Population Simulation Over Time')
        plt.show()

