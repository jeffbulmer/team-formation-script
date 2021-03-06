from social_network import SocialNet as SocialNet

class FASTT:
    """
    An instance of the Fair Allocation of Several Teams to Tasks is 
    given by:

    N = [n] a set of projects
    O = {o_1, o_2,...,o_m} a set of students
    G(O,E) = a graph representing the underlying social network
    R = {r_1,...r_n} the requirements for each project 
    S = {s_1,...,s_m} the skill sets for each employee
    U = the set of utility functions

    """

    _n = []
    _o = []
    _g = None
    _teams = []
    _u = []

    def __init__(self, projects, students):
        self._n = projects
        self._o = students
        self._g = SocialNet(self._o, True)
        for i in projects:
            self._teams.append({})
        self._u = self.evaluate_utilities(self._o)

    def evaluate_utilities(self, students):
        all_utilities = []

        for i in range(len(self._n)):
            project = self._n[i]
            utility = []
            current_skills = []
            if(len(self._teams) > i-1 and self._teams[i] is not None):
                for member in self._teams[i]:
                    current_skills = list(set(current_skills) & set(member.getSkills()))
            for student in self._o:
                usefulness = len(set(student.getSkills()) & (set(project.get_requirements())-set(current_skills)))
                d = self.diameter(self._teams[i], student)
                old_d = self.diameter(self._teams[i])
                if(d == 0 or d == old_d):
                    utility.append(usefulness)
                else:
                    utility.append(usefulness+(old_d-d))
            all_utilities.append(utility)
        return(all_utilities)

    def diameter(self, team, student=None):
        """
               Checks the diameter of a team as defined in Lappas et al. (2012)
               If a student is specified, the resulting diameter will be the diameter of the team
               after that student has been added. If no student is specified, then the diameter of
               the current team is returned.

               Parameters
               ----------
               team : list
                   A list of Student objects.
               student: Student
                   A single student to be added to a team.
                   Optional parameter

               Returns
               -------
               diameter : int
                   An integer representing the total edge weight of the
                   longest shortest path between any two individuals in the team
        """
        if(team is None):
            return 0
        elif(student is None):
            sn = SocialNet(team, True)
            diameter = sn.check_diameter()
            return diameter
        else:
            temp_team = team;
            temp_team.append(student)
            sn = SocialNet(temp_team, True)
            diameter = sn.check_diameter()
            return diameter

    def check_distance(self, team, verbose):
        sn = SocialNet(team, True)
        for i in range(len(team)):
            for j in range(len(team)):
                mat = sn.check_distance(team[i], team[j])

        print(mat)
