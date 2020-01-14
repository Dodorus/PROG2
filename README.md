# Rezäptbay

Aus verschiedenen, auch selber zusammengestellten Menüs, auswählen. Am Schluss erhält man eine Einkaufsliste von welchen Zutaten man was genau benötigt.

## Zu installierende Module aus Python (Python zeigt ja welche Module noch fehlen beim ersten Start der App)
flask
flask_login
datetime
json
flask_sqlalchemy
flask_bcrypt
flask_login
pymongo
os
secrets
PIL
wtforms_json
flask_wtf
wtforms

## Start

Anhand von Datenbanken (für Logins) und CSV Sheets ein System entwickeln, welches die definierten Anforderungen erfüllt.

## Anforderungen

- Einloggen, Registrieren und Abmelden
- Eigene Menüs erfassen und speichern
- Menüs zusammentragen und eine "Einkaufsliste" ausgeben, mit den genauen Mengen

![alt text](https://github.com/Dodorus/PROG2/blob/master/pages.png)

## Mögliche Navigation

Home, Menüs, Eigene Menüs erfassen, Warenkorb, Registrieren/Anmelden/Logout

## Ziele

1. Ziel: Webapp mit Navigation schreiben.
2. Ziel: Datenbank oder CSV aufsetzen und Daten manuell eintragen.
3. Ziel: Verwaltung der Daten über eine Webapp

# Wichtige Hinweise vom Januar 2020

Es folgen wichtige Hinweise zur Webapp von Dominic Kunz.

## Ziele

Die Ziele wurden bedingt erfüllt. Das implementieren von Mongo DB hat mehr Energie und Zeit verschluckt als erwartet. Dafür kann ich nun verschiedene "Datenbanken" von Mongo DB implementieren und selber Daten darin speichern sowie auslesen :)

## Weitere geplante Funktionen

1. Beim Einlesen der Rezepte muss darauf geachtet werden, dass keine Punkte mitgegeben werden. Dies ergibt ein Fehler in Flask. Ich hatte eine Funktion gebaut, die die Punkte rausnimmt und wieder einfügt, leider ist diese bei einem Merge von Github zerstört worden und die Zeit war mir nicht mehr genug um sie neu zu schreiben.
2. Aus der Wochenplanung können keine Rezepte rausgelöscht werden, auch diese Funktion fiel mehr oder weniger dem Merge zum Opfer. Leider bin ich auch nicht der Github pro, dass ich diese wieder hätte herstellen können. schade.
3. Natürlich müssten auch noch Informationen wie die Rezepte zubereitet werden hinzugefügt werden.
4. Eine Funktion, welche alle Zutaten der nächsten Woche in einen Warenkorb packt und einen Einkaufszettel ausspuckt, danach werden die Rezepte in eine andere "Sektion" geführt, welche momentan nicht existiert.