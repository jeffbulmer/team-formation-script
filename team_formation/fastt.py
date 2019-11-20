from SocialNetwork import SocialNet as SocialNet

class FASTT:
    """
    An instance of the Fair Allocation of Several Teams to Tasks is 
    given by:

    N = [n] a set of projects
    O = {o_1, o_2,...,o_m} a set of employees
    G(O,E) = a graph representing the underlying social network
    R = {r_1,...r_n} the requirements for each project 
    S = {s_1,...,s_m} the skill sets for each employee
    U = the set of utility functions

    """

    def __init__(self, projects, employees):
        self.n = projects
        self.o = employees
        self.g = SocialNet(o, True)