
Ich habe mich dazu entschieden in meinem Projekt eine Einkaufsliste umzusetzen, 
in der man Notizen für einzelne Dinge die man einkaufen muss niederschreiben kann. 
Ich habe mich für diese Funktion entschieden, 
da ich selbst sehr vergesslich bin und dieses Projekt einen tatsächlichen Nutzen hat. 
Zudem ist es möglich Notizen zu ändern oder zu löschen. 
Sind keine Notizen vorhanden, wird dies dem Nutzer angezeigt.


- Welche Optionen oder auch Spezialitäten existieren
    ```
  - Das Editieren von Notizen
  - Das Löschen von Notizen
  - Das Suchen von Notizen
  - Jede Notiz besitzt eine eigene reference id
    ```
Architektur
```
ERSTELLEN
post request mit information über notiz an server
-> wird formatiert in db hochgeladen (ref id)

SUCHEN
post request mit information über notiz an server
-> db eionträge werden ausgelesenn und richtiger durch for loop gefunden (ref id)

LÖSCHEN
get request mit ref id der noitz
-> wird aus dfb gelöscht

EDITIEREN
get request mit ref id der noitz
noitz wird in der db ausgelesen
-> edit.html 
```
