# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab
import copy

'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        # print("clearProb", clearProb)
        # print("getMaxBirthProb():", self.getMaxBirthProb())

    def getMaxBirthProb(self):
        """
        Returns maximum reproduction probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns maximum clearance probability.
        """
        return self.clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        # TODO

        # print("self.getClearProb(): {}".format(str(self.getClearProb())))
        if random.random() < self.getClearProb():
            # print("doesClear value: True")
            # print("doesClear() returns: True")
            return True
        else:
            # print("doesClear value: False")
            # print("doesClear() returns: False")
            return False


    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO
        if random.random() < self.getMaxBirthProb() * (1 - popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException




class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        # TODO

        self.viruses = viruses
        # print("self.viruses:", self.viruses)
        self.maxPop = maxPop
        self.test = 0

    def updateViruses(self, viruses):
        """
        Updates virus list
        """
        self.viruses = viruses


    def getMaxPop(self):
        """
        Returns the maximum virus population the patient can have.
        """
        return self.maxPop

    def getTotalPop(self):

        """
        Gets the current total virus population.
        returns: The total virus population (an integer)
        """

        # TODO

        return len(self.viruses)


    def update(self, activeDrugs=[]):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.
        - The current population density is calculated. This population density
          value is used until the next call to update()
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO

        viruses = copy.copy(self.viruses)
        # print("viruses", viruses)

        for virus in viruses:
            # print("virus:", viruses)
            # assert virus != None, "at PS7's update() method"
            clear_Value = virus.doesClear()
            if clear_Value == True:
                if clear_Value == False:
                    print("virus.doesClear() =", virus.doesClear(), "and virus removed.")
                viruses.remove(virus)
            else:
                popDensity = self.getTotalPop() / self.getMaxPop()
                try:
                    John = virus.reproduce(popDensity, activeDrugs)
                    # assert John != None, "Gotcha, ya bitch!"
                    # if John == None: input("John = {}".format(str(John)))
                    if John != None: viruses.append(John)
                except NoChildException:
                    continue

        self.updateViruses(viruses)




#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.
    """

    # TODO
    herpes = []
    evolving_herpes_pop = []
    for herp_derp in range(100):
        herpes.append(SimpleVirus(0.2, 0.1))
    # print(herpes)

    Sydney = SimplePatient(herpes, 1000)
    print(Sydney.getTotalPop())

    for time in range(300):
        Sydney.update()
        evolving_herpes_pop.append(Sydney.getTotalPop())
        # print("evolving_herpes_pop", evolving_herpes_pop)


    print(Sydney.getTotalPop())

    pylab.title('Herpes Population Over 300 Reproductive Cycles')
    pylab.xlabel('Cycle')
    pylab.ylabel('Total Population')
    pylab.plot(range(300), evolving_herpes_pop)
    pylab.figure()

#for trial in range(10):
    #simulationWithoutDrug()
#pylab.show()

#
# PROBLEM 3
#
