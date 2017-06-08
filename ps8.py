# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:



import numpy
import random
import pylab
import copy
from ps7 import *

class RepeatDrugException(Exception):
    """
    RepeatDrugException is raised by the addPrescription() method in the Patient
    class to indicate that a duplicate drug was attempted and prevented.
    """

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb, **kwargs):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.

        """


        # TODO

        super(type(self), self).__init__(maxBirthProb, clearProb, **kwargs)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns current resistances to specific drugs
        """

        return self.resistances

    def setRestistance(self, drug, value):
        """
        Sets the resistance of a drug to a given value
        """
        self.resistances[drug] = value

    def getMutProb(self):
        """
        Returns the probability of mutating--and thus gaining resistance to a
        specific drug.
        """
        return self.mutProb

    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """

        # TODO
        return self.resistances[drug]


    def reproduce(self, popDensity=0.1, activeDrugs={}):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        # TODO

        # if True not in self.resistances.values()
        if True not in [self.isResistantTo(drug) for drug in self.getResistances()]:
            if random.random() < self.getMaxBirthProb() * (1 - popDensity):
                offspring_virus = copy.copy(self)
                # print("offspring_virus:", offspring_virus)
                for drug in activeDrugs: # offspring_virus.resistances.keys():
                    if random.random() < 1 - offspring_virus.getMutProb():
                        continue
                    else:
                        # print(self.getResistances())
                        try:
                            offspring_res = not self.getResistances()[drug]
                            offspring_virus.setRestistance(drug, offspring_res)
                        except KeyError:
                            print("Here's why there's a KeyError")
                            print("Keys:", self.getResistances().keys())
                # print("offspring_virus:", offspring_virus)
                # assert offspring_virus != None, "At method reproduce()"
                return offspring_virus



class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop, **kwargs):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: the list representing the virus population (a list of
        ResistanteVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        super(type(self), self).__init__(viruses, maxPop)
        self.activeDrugs = []

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        # should not allow one drug being added to the list multiple times
        if newDrug not in self.getPrescriptions():
            self.activeDrugs.append(newDrug)
            print("Prescription, {} added...".format(newDrug))
            print("patient.getPrescriptions()", self.getPrescriptions())
        else:
            print(newDrug, "already administered.")

    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO
        return self.activeDrugs

    def getViruses(self):
        """
        Returns the list of viruses
        """
        return self.viruses

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        res_viruses = 0

        for virus in self.getViruses():
            for drug in drugResist:
                # print("virus.getResistances():", virus.getResistances())
                if virus.getResistances()[drug]:
                    res_viruses += 1

        return res_viruses


    def update(self, activeDrugs):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO

        return super(type(self), self).update(activeDrugs)

#
# PROBLEM 2
#

def startingViri():
    herpes = []
    for herp_derp in range(100):
        herpes.append(ResistantVirus(0.1, 0.05, {"guttagonol":False, "grimpex":False}, 0.005))
    return herpes

def updateData(patient, amt, data1=None, data2=None, data3=None, data4=None):
    for time in range(amt):
        patient.update(patient.getPrescriptions())

        # If continuous, uncomment
        data1.append(patient.getTotalPop())
        data2.append(patient.getResistPop(["guttagonol"]))
        data3.append(patient.getResistPop(["grimpex"]))
        data4.append(patient.getResistPop(["guttagonol", "grimpex"]))


def updateContinuousData(patient, data1, data2, data3, data4, delay=150, trial_num=1):

    # Trial One
    if trial_num == 1:
        updateData(patient, 150, data1, data2, data3, data4)
        patient.addPrescription("guttagonol")

        updateData(patient, 300, data1, data2, data3, data4)
        patient.addPrescription("grimpex")

        updateData(patient, 150, data1, data2, data3, data4)

    # Trial Two
    if trial_num == 2:
        updateData(patient, 150, data1, data2, data3, data4)
        patient.addPrescription("guttagonol")
        patient.addPrescription("grimpex")

        updateData(patient, 300, data1, data2, data3, data4)


def simulationWithDrug(num_trials=None, delay=None, fignum=None):

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO

    # herpes_list = [startingViri() for x in range(num_trials)]
    evolving_herpes_pop = []
    evolving_gut_res_herpes_pop = []
    evolving_gri_res_herpes_pop = []
    evolving_mult_res_herpes_pop = []

    evolving_average_herpes_pop = []
    evolving_average_gut_res_herpes_pop = []
    Sydney = Patient(startingViri(), 1000)
    Peter_Sr = Patient(startingViri(), 1000)
    # patients = [Patient(herpes_list[x], 1000) for x in range(num_trials)]

    # print(Sydney.getTotalPop())
    # print("Sydney.getPrescriptions()", Sydney.getPrescriptions())

    # updateData(Sydney, evolving_herpes_pop, evolving_gut_res_herpes_pop, 150)
    # Sydney.addPrescription("guttagonol")
    #
    # print("Sydney.getTotalPop()", Sydney.getTotalPop())
    # print("Prescription, guttagonol added...")
    # print("Sydney.getPrescriptions()", Sydney.getPrescriptions())
    #
    # # updateData(Sydney, evolving_herpes_pop, evolving_gut_res_herpes_pop, 150)

    # updateAverageData(patients, evolving_average_herpes_pop, evolving_average_gut_res_herpes_pop, delay)
    updateContinuousData(Sydney, data1=evolving_herpes_pop, data2=evolving_gut_res_herpes_pop,
                    data3=evolving_gri_res_herpes_pop, data4=evolving_mult_res_herpes_pop, delay=150, trial_num=1)

    # print("Sydney.getTotalPop()", Sydney.getTotalPop())
    pylab.figure()
    pylab.title('Analysis of Virus Population Dynamics with Two Drugs (Separate Times)'.format(delay))
    pylab.xlabel('Cycle #')
    pylab.ylabel('Population')

    pylab.plot(range(len(evolving_herpes_pop)), evolving_herpes_pop, label="Total")
    pylab.plot(range(len(evolving_gut_res_herpes_pop)), evolving_gut_res_herpes_pop, label="Gut-Res")
    pylab.plot(range(len(evolving_gri_res_herpes_pop)), evolving_gri_res_herpes_pop, label="Gri-Res")
    pylab.plot(range(len(evolving_mult_res_herpes_pop)), evolving_mult_res_herpes_pop, label="Mult-Res")
    pylab.legend(loc='upper right')

    evolving_herpes_pop = []
    evolving_gut_res_herpes_pop = []
    evolving_gri_res_herpes_pop = []
    evolving_mult_res_herpes_pop = []

    updateContinuousData(Peter_Sr, data1=evolving_herpes_pop, data2=evolving_gut_res_herpes_pop,
                        data3=evolving_gri_res_herpes_pop, data4=evolving_mult_res_herpes_pop, delay=150, trial_num=2)

    pylab.figure()
    pylab.title('Analysis of Virus Population Dynamics with Two Drugs (Same Time)'.format(delay))
    pylab.xlabel('Cycle #')
    pylab.ylabel('Population')
    # pylab.axis([0, 1000, 0, 50])

    # a,b = pylab.polyfit(range(len(evolving_average_herpes_pop)), evolving_average_herpes_pop, 1)
    # c,d = pylab.polyfit(range(len(evolving_average_herpes_pop)), evolving_average_gut_res_herpes_pop, 1)
    # pylab.plot(a, b)
    # pylab.plot(c, d)
    # pylab.subplot(int("22" + str(fignum)))
    # data = evolving_average_herpes_pop
    # pylab.xticks(numpy.arange(0, 1000, 100))
    # pylab.yticks(numpy.arange(0, 50, 5))
    # binBoundaries = numpy.linspace(0,1000,20)
    # pylab.hist(data, bins=binBoundaries) #, bins=range(min(data), max(data) + binwidth, binwidth))
    # pylab.plot(range(len(evolving_average_herpes_pop)), evolving_average_herpes_pop)
    # pylab.plot(range(len(evolving_average_herpes_pop)), evolving_average_gut_res_herpes_pop)

    pylab.plot(range(len(evolving_herpes_pop)), evolving_herpes_pop, label="Total")
    pylab.plot(range(len(evolving_gut_res_herpes_pop)), evolving_gut_res_herpes_pop, label="Gut-Res")
    pylab.plot(range(len(evolving_gri_res_herpes_pop)), evolving_gri_res_herpes_pop,label="Gri-Res")
    pylab.plot(range(len(evolving_mult_res_herpes_pop)), evolving_mult_res_herpes_pop, label="Mult-Res")
    pylab.legend(loc='upper right')


# Try except every variable, if it works, good. IF not, give me a chance to put the right variable in.



# Average Trial
# for trial_size in [300, 150, 75, 0]:
#     fignum = [300, 150, 75, 0].index(trial_size) + 1
#     simulationWithDrug(100, trial_size, fignum)
#     print("fignum:", fignum)
#for trial in range(10):
    #simulationWithoutDrug()
simulationWithDrug()
pylab.show()

#
# PROBLEM 3
#

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
    """

    # TODO

#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    # TODO



#
# PROBLEM 5
#

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.

    """
    #TODO
