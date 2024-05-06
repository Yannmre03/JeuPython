import csv

def fonction_Sortie(nomF, ScoreF):
    row = [nomF, ScoreF]
    with open('Scores.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
def fonction_afficher_scores():
    Scores = []
    with open('Scores.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            Scores.append(row)
    return Scores
score = fonction_afficher_scores()
scoreBis = []
for i in range(len(score)):
    cmpt = len(score)-i
    scoreBis.append = score[cmpt-1]
print(score)
print("\n")
print(scoreBis)