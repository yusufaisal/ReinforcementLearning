import pandas as pd

class q_learning:
    reward = []
    def __init__(self,path):
        self.__loadReward(path)

    def __loadReward(self,path):
        self.reward = pd.read_csv(path,sep='\s+',header=None)

    def run(self):
        None