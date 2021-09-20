dag = input("Kies weekdag:").lower()

if dag == "maandag":
    dag = 1
if dag == "dinsdag":
    dag = 2
if dag == "woensdag":
    dag = 3
if dag == "donderdag":
    dag = 4
if dag == "vrijdag":
    dag = 5
if dag == "zaterdag":
    dag = 6
if dag == "zondag":
    dag = 7
score = 1
while score <= dag:
    if score == 1:
        naam = "Maandag"
    if score == 2:
        naam = "Dinsdag"
    if score == 3:
        naam = "Woensdag"
    if score == 4:
        naam = "Donderdag"
    if score == 5:
        naam = "Vrijdag"
    if score == 6:
        naam = "Zaterdag"
    if score == 7:
        naam = "Zondag"
    print(naam)
    score = score + 1