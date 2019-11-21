class SocialNet:

    _socialNetwork = {}
    _labels = []

    def __init__(self, students, balance):
        self._socialNetwork = self.createSocialNetwork(students);
        self._labels = self.setLabels(students)
        if(balance is True):
            self._socialNetwork=self.balanceNetwork(self._socialNetwork)

    def createSocialNetwork(self, students):
        names = []
        network = {}

        for s in students:
            names.append(s.getName())

        for i in range(len(students)):
            b = students[i].getBestFriend()
            f = students[i].getFriends()
            e = students[i].getEnemies()
            curr_row = [];
            for j in range(len(students)):
                if j == i:
                    curr_row.append(0)
                elif names[j] is b:
                    if(students[j].getBestFriend() is names[i]):
                        curr_row.append(1)
                    else:
                        curr_row.append(5)
                elif names[j] in f:
                    curr_row.append(3)
                elif names[j] in e:
                    curr_row.append(7)
                else:
                    curr_row.append(5)
            network[students[i].getName()] = curr_row

        return network

    def setLabels(self, students):
        labels = []
        for s in students:
            labels.append(s.getName())
        return labels

    def balanceNetwork(self, socialNetwork):
        names = self._labels;
        for k in range(len(names)):
            for i in range(len(socialNetwork[names[k]])):
                if(socialNetwork[names[k]][i] != socialNetwork[names[i]][k]):
                    socialNetwork[names[k]][i] = max(socialNetwork[names[k]][i], socialNetwork[names[i]][k])
                    socialNetwork[names[i]][k] = max(socialNetwork[names[k]][i], socialNetwork[names[i]][k])

        return socialNetwork



