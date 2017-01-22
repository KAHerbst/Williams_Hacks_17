import csv

MAJORS = ["American Studies", "Anthropology", "Arabic Studies", "Art (History)",
          "Art(Studio)", "Art (History and Practice)", "Asian Studies", "Astronomy",
          "Astrophysics", "Biology", "Chemistry", "Chinese", "Classics (Greek & Latin) Language",
          "Classics (Greek & Latin) Civilization", "Comparative Literature Track 1", "Comparative Literature Track 2",
          "Computer Science", "Economics", "English", "Environmental Policy", "Environmental Science",
          "French", "Geosciences","German","History","Japanese","Math","Music","Philosophy",
          "Physics","Political Economy","Political Science","Psychology","Religion","Russian",
          "Sociology","Spanish","Statistics","Theatre","Women's, Gender, & Sexuality Studies"]
major = query
with open("data.csv") as fin:
    f1 = list(csv.reader(fin))
    for line in f1:
        if line[0] == major:
            return line[1:]