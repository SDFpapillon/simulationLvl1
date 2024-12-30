dt = 100 #100 is the maximum, after aproximation is too big

class Object:

    """
    I'm a French man, I want to name this class "astre" but I don't know the english word for this... sry

    Here, I'll define object and all function for this

    I juste want some "little" function :
        - force sum (universe send all force to all Object)
        - self evolution


    """

    def __init__(self, masse, position, speed):

        self.masse = masse
        self.forces = []
        self.acceleration = [0, 0]
        self.speed = [speed[0] * (dt**0.5), speed[1] * dt ** 0.5]
        self.position = position


    def calcMyAcceleration(self):

        if self.masse != 0 :
            totalForces = [0,0]

            for force in self.forces:
                for i in range(2):
                    totalForces[i] += force[i]

            self.forces = []

            for i in range(2):
                self.acceleration[i] = (dt * totalForces[i] / abs(self.masse))

        else :
            self.acceleration = [0, 0]


    def evolution(self):

        for i in range(2):
            self.position[i] += dt * self.speed[i]

        for i in range(2):
            self.speed[i] += dt * self.acceleration[i]
