import csv


def fonction_open_csv():
    contenu  = []
    positive = []
    negative = []
    with open("Situations.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contenu.append(row)
        for i in range(len(contenu)):
            if contenu[i][0] == "Positive":
                positive.append(contenu[i][1:-1])
            if contenu[i][0] == "Negative":
                negative.append(contenu[i][1:-1])
    return positive, negative
pos, neg = fonction_open_csv()
print(pos)