class Task: 
    """
    A class to describe a task.

    Attributes
    ----------
    name : str
        The name of the task.
    reqs : list
        A list of strings that describe the requirements of the Task. 

    Methods
    -------

    """

    _name="";
    _reqs=[];

    def __init__(self, name="Groupwork", reqs=[]):
        self._name = name
        self._reqs = reqs

    def get_requirements(self):
        return self._reqs

    def check_cover(self, team):
        """
        Checks how many requirements of a task are met by a group, i.e 
        the coverage of a group over a task.
        Analogous to the checkMaxCover method within the JAVA code
        
        Parameters
        ----------
        team : list
            A list of Student objects. 
        
        Returns
        -------
        coverage : double
            A double representing the percentage of the task requirements
            which are covered by the team.
        """
        # valid = True
        covered = [];

        if len(self._reqs) == 0:
            coverage = 1;
        elif team.len() == 0:
            coverage = 0;
        for i in team:
            # get the union of all student skills
            covered = covered + i.getSkills();

        # get the intersection of all student skills and the task requirements
        covered = list(set(covered) & set(self._reqs))
        coverage = len(covered) / len(self._reqs);
        return coverage
