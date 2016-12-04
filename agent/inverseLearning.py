import numpy as np
from approximateAgents import *

class inverseLearning:
    """docstring for inverseLearning"""
    def __init__(self, agent, numEstimating, numTraining):
        self.agent = agent
        self.gamma = agent.getGamma()
        self.numEstimating = numEstimating
        self.numTraining = numTraining

        self.featureSize = 0
        self.w = np.zeros((self.featureSize,1))
        self.mus = []
        self.muBar = None
        self.muExpert = None
        
        pass
        
    def train(self):
        self.featureExpectation()
        t = self.updateRewardFunction()

        while t > self.error:
            self.updateAgent()
            self.featureExpectation()
            t = self.updateRewardFunction()

    # override this function
    def computeExpertExpectation(self):
        pass

    def featureExpectation(self):
        self.agent.setMode(AgentMode.estimating)
        mu = np.zeros((self.featureSize, 1))
        for i in range(self.numEstimating):
            self.runGame()
<<<<<<< HEAD
            mu += self.agent.getfeatureExpection()
        self.mus.append(mu / numEstimating)
=======
            miu += self.agent.getfeatureExpectation()
        self.mius.append(miu / numEstimating)
>>>>>>> 7622421ec4255f9522fe6b322d9d2cfc67214b90

    def updateRewardFunction(self):
        if self.muBar = None:
            self.muBar = self.mus[0]
            muBar = self.muBar
        else:
            coef = (self.mus[-1] - self.muBar).T.dot(self.muExpert - self.muBar)
            coef = coef / (self.mus[-1] - self.muBar).T.dot(self.mus[-1] - self.muBar)
            muBar = self.muBar + coef * (self.mus[-1] - self.muBar)
        self.w = self.muExpert - muBar
        self.muBar = muBar
        self.agent.setRewardVector(self.w)
        return np.linalg.norm(self.w)
        
    def updateAgent(self):
        self.agent.setMode(AgentMode.training)
        for i in range(self.numTraining):
            self.runGame()

    # override this function
    def runGame(self):
        pass