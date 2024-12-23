from object import Object

class Universe:

    def __init__(self, objects):
        self.objects = objects
        self.G = 6.67430 * 10**(-11)

    def NewtonLaw(self, objectCalc):

        """
        calc the Newton force applied by the universe on "objectCalc"

        :param objectCalc:
        :return:
        """

        for object in self.objects:
            vect = [0, 0]

            for i in range(2):
                vect[i] = object.position[i] - objectCalc.position[i]

            if vect[0] != 0 or vect[1] != 0:
                norm = 0

                for i in range(2):
                    norm += vect[i] ** 2

                norm = norm ** 1.5

                for i in range(2):
                    vect[i] *= self.G * object.masse * objectCalc.masse
                    vect[i] /= norm

            objectCalc.forces += [vect]


    def evolution(self):

        for object in self.objects:
            self.NewtonLaw(object)

        for object in self.objects:
            object.calcMyAcceleration()
            object.evolution()

