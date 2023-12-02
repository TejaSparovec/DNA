hair = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
face = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
eyes = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

people = {"eva" : ["female", "white", "blonde", "blue", "oval"],
          "larisa" : ["female", "white", "brown", "brown", "oval"],
          "matej" : ["male", "white", "black", "blue", "oval"],
          "miha" : ["male", "white", "brown", "green", "square"]}

with open ("dna.txt","r") as dna_file:
    dna=str(dna_file.read())

person=[]

for i in gender:
    if gender[i] in dna:
       print(i)
       person.append(i)
for i in race:
    if race[i] in dna:
        print(i)
        person.append(i)
for i in hair:
    if hair[i] in dna:
        person.append(i)
for i in eyes:
    if eyes[i] in dna:
        person.append(i)
for i in face:
    if face[i] in dna:
        person.append(i)

print(person)

for p in people:
    if people[p] == person:
        print(f"Osumljenec je {p}")






