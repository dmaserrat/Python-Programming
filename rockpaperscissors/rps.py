def rps(p1,p2):
        choice = {"rock": 0, "paper": 1, "scissors": 2}
        result = ["Draw!","P1 Wins!","P2 Wins!"]

        return print(result[choice[p1] - choice[p2]])
