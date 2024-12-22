class Object:

    """
    I'm a French man, I want to name this class "astre" but I don't know the english word for this... sry

    Here, I'll define object and all function for this

    I juste want some "little" function :
        - force sum (universe send all force to all Object)
        - self evolution


    """

    def __init__(self, masse, dimension, position, speed):

        self.masse = masse
        self.dimension = dimension #all objects are a spher
        self.forces = []
        self.acceleration = []
        self.speed = speed
        self.position = position


    def calcMyAcceleration(self):

        totalForces = [0,0,0]

        for force in self.forces:
            for i in range(3):
                totalForces[i] += force[i]

        self.forces = []

        for i in range(3):
            self.acceleration = totalForces[i] / self.masse


    def evolution(self):

        for i in range(3):
            self.position[i] += self.speed[i]

        for i in range(3):
            self.speed[i] += self.acceleration[i]