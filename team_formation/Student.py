class Student:

    _name = ""
    _skills = []
    _friends = []
    _enemies = []
    _preferences = []
    _best_friend = ""


    def __init__(self, name, skills, friends, enemies, preferences, bestfriend):
        self._name = name;
        self._skills = skills;
        self._friends = friends;
        self._enemies= enemies;
        self._preferences = preferences;
        self._best_friend = bestfriend

    def getName(self):
        return(self._name)

    def getSkills(self):
        return(self._skills)

    def getFriends(self):
        return(self._friends)

    def getEnemies(self):
        return(self._enemies)

    def getPreferences(self):
        return(self._preferences)

    def getBestFriend(self):
        return(self._best_friend)





