#Diese Modul öffnet ein Eingabefenster für Login Daten unter Verwendung von PyQt5.

##Über Parameter kann Festgelegt werden, ob nur ein Passwort, oder auch Passwort wiederholen oder Username Eingabefelder erstellt werden sollen.
###Der Bestätigungsbutton kann erst gedrückt werden, wenn alle vorgegebenen Felder ausgefüllt worden sind.

####Wenn der Bestätigungsbutton gedrückt wird, wird eine mitgegebene Funktion aufgerufen, die egal welche Felder aktiv sind die Werte Username, Passwort liefert. 
#####Falls kein Username abgefragt wurde, ist dieser Parameter None.

######Auch können alle Strings des Fensters angepasst werden, indem man ein dictionary mit den Strings in config mitgibt.