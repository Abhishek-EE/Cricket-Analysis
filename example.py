from cricsummary.cricsummary import Duranz
match = Duranz('data/587475.json')
match.scorecard(team=1)
match.plot_manhattan(team=1)
