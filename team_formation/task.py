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

    def __init__(self, name, reqs):
        self.name = name
        self.reqs = reqs

    def check_cover(self, team):
        """
        Checks how many requirements of a task are met by a group, i.e 
        the coverage of a group over a task.
        
        Parameters
        ----------
        team : list
            A list of Student objects. 
        
        Returns
        -------
        valid : bool
            A boolean flag saying whether it's valid. 
        """
        valid = True
        if team.len() == 0:
            valid = False
        for i in range(0, self.reqs.len()):
            for j in range(0, team.len()):
                if team[j].getSkills()