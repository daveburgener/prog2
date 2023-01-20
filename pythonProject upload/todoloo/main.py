from flask import render_template
from werkzeug.utils import redirect
from flask import Flask, request, redirect
from todoloo.datenbank import abspeichern, todos_laden, suchen, auslesen, suchen_mit_ref_id

app = Flask(__name__)
app.secret_key = 'the random string'


@app.route("/")
@app.route("/index", methods=["GET"])

def route_index():
    # geben gerenderte website zurück
    return render_template("index.html", liste=todos_laden(), seitentitel="Start")

@app.route("/add", methods=["GET", "POST"])
def route_add():
    if request.method == "GET":
        return render_template("add.html", seitentitel="Eingabe")

    if request.method == "POST":
        text = request.form['text']
        # .strip entfernt whitespaces an ende und anfang einer string
        if not text.strip():
            return redirect("/add")
        # sonst speichern wir den neuen eintrag ab
        abspeichern(text)

        return redirect("/")

@app.route("/search.html", methods=["GET", "POST"])
def route_search():
    if request.method == "GET":
        return render_template("search.html", seitentitel="Suchen")

    if request.method == "POST":
        text = request.form['text']
        ergebnis = suchen(text)
        return render_template("index.html", liste=ergebnis)

@app.route("/delete", methods=["GET"])
def route_delete():
    # http://127.0.0.1:5591/delete?ref_id=<ref_id>
    ref_id = request.args.get("ref_id")

    content = auslesen().splitlines()
    # wir loopen durch alle einträge der datenbank und ignorieren den der mit ref_id beginnt
    new_content = [eintrag for eintrag in content if not eintrag.startswith(ref_id)]
    # überschreiben datenbank mit new_content
    with open("database.csv", "w") as f:
        # wir haben vorher alle zeilen getrennt und fügen diese jetzt wieder zusammen
        f.write("\n".join(new_content))
    # redirect auf homepage
    return redirect("/")

@app.route("/edit", methods=["GET", "POST"])
def route_edit():
    if request.method == "GET":
        # http://127.0.0.1:5591/delete?ref_id=<ref_id>
        ref_id = request.args.get("ref_id")
        # suchen des eintrags mit id
        eintrag = suchen_mit_ref_id(ref_id)
        print(ref_id, eintrag)
        return render_template("edit.html", seitentitel="Bearbeiten", eintrag=eintrag)

    if request.method == "POST":
        # http://127.0.0.1:5591/delete?ref_id=<ref_id>
        text = request.form["text"]
        ref_id = request.form["ref_id"]

        einträge = auslesen().splitlines()
        new_content = []
        # loopen durch alle einträge
        for eintrag in einträge:
            # teilen eintrag am komma
            eintrag = eintrag.split(",")
            if eintrag[0] == ref_id:
                eintrag[2] = text
                new_content.append(",".join(eintrag))
                continue
            # andernfalls wird der eintrag einfach in die neue liste übernommen
            new_content.append(",".join(eintrag))
        with open("database.csv", "w") as f:
            f.write("\n" + "\n".join(new_content))
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5551)
