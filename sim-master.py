import argparse
import numpy as np

DEFAULT_TRIALS = 10 # number of times to run each algorithm

class TeamBanditModel:
    """ A container class for all parameters needed for playing the team bandit """
    horizon = None
    skill_space = None
    latent_space = None
    mapping = None
    task = None
    team_native = None

    def __init__(self):
        print("Created blank team bandit model instance.")


    """
    T is the time horizon of the bandit
    """
    def set_horizon(self,T):
        self.horizon = T
    def get_horizon(self):
        return self.horizon

    """ 
    A is a numpy 2xN array, where each pair of entries corresponds to lower/upper bounds on skill space
    """
    def set_skill_space(self,A):
        self.skill_space = A
    def get_skill_space(self):
        return self.skill_space


    """
    a is an MxN list of skill vectors, aka a native representation of the team
    """
    def set_team(self,S):
        self.team_native = S
    def get_team(self):
        return self.team_native

    """ 
    B is a numpy 2xN array, where each pair of entries corresponds to lower/upper bounds on latent space
    """
    def set_latent_space(self,B):
        self.latent_space = B
    def get_latent_space(self):
        return self.latent_space


    """
    M is an NxK matrix which maps skill space to latent space 
    """
    def set_true_mapping(self,M):
        self.mapping = M
    def get_true_mapping(self):
        return self.mapping 

    """
    t is a point in R^k (latent space)  
    """
    def set_true_task(self,t):
        self.task = t
    def get_true_task(self):
        return self.task



def create_model(name):
    print("Creating model with name " + name)
    
    model = TeamBanditModel()

    horizon = None
    skill_space = None
    latent_space = None
    mapping = None
    task = None
    teams = None

    if (name.startswith("test")):
        if (name.startswith("test-1")):
            horizon = 20
            skill_space = np.array([[0,0,0],[1,1,1]])
            latent_space = np.array([[0,0],[3,3]])
            mapping = np.array([[1,1],[1,1],[1,1]])
            task = np.array([2,2])
        else:
            print ("No such name '" + name + "' for model creation routine, exiting")
            exit()
    else:
        print ("No such name '" + name + "'for model creation routine, exiting")
        exit()

    model.set_horizon(horizon)
    model.set_skill_space(skill_space)
    model.set_latent_space(latent_space)
    model.set_true_mapping(mapping)
    model.set_true_task(task)
            

    return model


def run_trial(model, alg_name):
    
    horizon = model.get_horizon()
    

        

if __name__ == "__main__":
  
    parser = argparse.ArgumentParser(description='Team Bandit simulation')
    parser.add_argument('--name',help='name of the simulation to run')
    parser.add_argument('--alg',help='name of the algorithm(s) to test, seperated by commas')
    parser.add_argument('--trials',help='number of repetitions to run each algorithm')
    args = parser.parse_args()

    if (args.name):
        print("Starting simulation (name=" + args.name + ")")
    else:
        print("Empty name of simulation, exiting")
        exit()

    if (args.alg):
        print("Starting simulation (alg=" + args.alg + ")")
    else:
        print("Empty algorithm selection, exiting")
        exit()

    if (args.trials):
        print("Running each algorithm for " + args.trials + " trials.")
    else:
        print("Using default number of trials ( "+ str(DEFAULT_TRIALS) + " )")
        


    
    name = args.name
    algs = args.alg
    algs = algs.split(",")
    print ("Name = " + name + "; algs = ",)
    print(algs)

    if (args.trials):
        trials = int(args.trials)
    else:
        trials = DEFAULT_TRIALS


    #construct model 
    model = create_model(name)

    #test algorithms
    results = {}
    for a in algs: #iterate over the algorithms
        results[a] = []
        print("Starting simulation of algorithm " +a)

        for t in range(trials): #try over number of trials
            trial_result = run_trial(model,a)
            results[a].append(trail_result)
            print("Finished trial "+ t)

        print("Finished simulation of algorithm " +a)
            
    #compile results 

    print("Simulation finished.")
