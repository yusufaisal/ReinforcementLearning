import pandas as pd

class q_learning:
    reward = []
    Q = None
    def __init__(self,path):
        self.__loadReward(path)
        data = [[0 for _ in range(len(self.reward)**2)] for _ in range(4)]
        self.Q = pd.DataFrame(data,columns=None)


    def __loadReward(self,path):
        self.reward = pd.read_csv(path,sep='\s+',header=None)

    def run(self):
        print(self.Q)