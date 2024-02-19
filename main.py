from my_classes import PopulationSimulator


simulator = PopulationSimulator(start_population=160, infant_mortality=5, youth_mortality=5, agriculture=5, disaster_chance=10, fertilityx=18, fertilityy=35)
simulator.simulate()
