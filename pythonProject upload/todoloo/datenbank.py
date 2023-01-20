import random
from datetime import datetime
from string import ascii_letters, digits

ALLOWED_FOR_REF_ID = ascii_letters + digits
DATENBANK_FP = "database.csv"

# generiert ref_id
def generate_ref_id():
    return "".join(random.choices(population=ALLOWED_FOR_REF_ID, k=10))

# generiert einzigartige ref_id
def generate_unique_ref_id(einträge):
    while True:
        # (string) generieren wir uns eine ref id
        ref_id = generate_ref_id()
        if not any([eintrag.split(",")[0] == ref_id for eintrag in einträge]):
            # beendet den loop und gibt die einzigartige ref_id zurück
            return ref_id

def auslesen():
    with open(DATENBANK_FP, "r") as open_file:
        inhalt = open_file.read()[1:]  # oder nutze .strip
    return inhalt

def todos_laden():
    return [eintrag.split(",") for eintrag in auslesen().splitlines()]

def abspeichern(notiz, datum: str = None, ref_id: str = None):
    einträge = auslesen()
    if not datum:
        datum = datetime.now().strftime("%Y-%m-%d %H:%M")
    # .splitlines unterteilt die datenbank in linien bzw. einträge
    if not ref_id:
        ref_id = generate_unique_ref_id(einträge.splitlines())
    neuer_eintrag = f"\n{ref_id},{datum},{notiz}"  # anstatt "\n" + ref_id + "," + datum + "," + noitz
    # .append fügt ein (anstatt den bestehenden neuer_eintrag zu "überschreiben, löschen")
    with open(DATENBANK_FP, "a") as open_file:
        open_file.write(neuer_eintrag)

def suchen(text):
    # wir lesen die einträge aus
    current_content = auslesen()
    search_result = []
    for row in current_content.splitlines():
        # teilen eintrag am komma
        eintrag = row.split(",")
        if text.lower() in eintrag[2].lower():
            search_result.append(eintrag)
    return search_result

def suchen_mit_ref_id(ref_id):
    content = auslesen()
    for row in content.splitlines():
        eintrag = row.split(",")
        if ref_id == eintrag[0]:
            return eintrag