# Enthält ein Passwort Fenster zum eingeben von Username, Passwort und Passwort wiederholen Fenster nach Wahl
###Haupt Klasse
####class PasswortMainWindow(QWidget):

    // __init__
    // Nimmt die Argumente:
    //   * function, eine Funktion, die ausgeführt wird, wenn bestätigt wird
    //   * window_konfiguration, eine Instantz der Klasse WindowKonfiguration, mit der die generellen Einstellungen zum Fenster gemacht werden
    //   * submit_widget, eine Instantz der Klasse SubmitWidgetStrings, mit der der Submit Button eingestellt wird
    //   * user_widget, falls gesetzt eine Instantz der Klasse UserWidgetStrings, zur Konfiguration, falls nicht gesetzt wird kein User Widget erstellt
    //   * passwort_widget, eine Instantz der Klasse PasswortWidgetStrings, erstellt falls gesetzt ein Passwort Widget
    //   * passwort_wiederholen_widget, eine Instantz der Klasse PasswortWidgetStrings, erstellt falls gesetzt ein zweites Passwort Widget
    def __init__(self,
                 function,
                 window_konfiguration: WindowKonfiguration,
                 submit_widget: SubmitWidgetStrings,
                 user_widget: UserWidgetStrings = None,
                 passwort_widget: PasswortWidgetStrings = None,
                 passwort_wiederholen_widget: PasswortWidgetStrings = None,
                 icon: QIcon = None,
                 minimum_width: int = None,
                 minimum_height: int = None)
    
    // reset
    // Nimmt keine Argumente
    // Und setzt die Werte aller Widgets zurück
    def reset(self)

------------------------------------------------------------------------------------------------------------------------
##Usernameeingabe-Widget

###Erstellt ein Eingabefeld für einen Benutzernamen
####class __UserEingabeWidget(QLineEdit):

    // __init__
    // Nimmt die Argumente:
    //   * confi, ein dictionary der Struktur:
    //   * onreturn, eine Funktion, die ausgeführt wird, wenn im Feld Enter gedrückt wird
    //   * on_text_changed, eine Funktion, die Ausgeführt wird, wenn sich der Text des Feldes ändert
    def __init__(self, config: dict, onreturn=None, on_text_changed=None)
    
    // set_from_config
    // Nimmt das Argument:
    //   * config, eine Instantz der Klasse UserEntryStrings
    def set_from_config(config: UserEntryStrings)
    
    // reset
    // Nimmt keine Argumente
    // Und setzt den Text zurück
    def reset(self)
    
    // set
    // Nimmt das Argument text
    // Und setzt den Wert des Feldes darauf
    def set(self, text)

------------------------------------------------------------------------------------------------------------------------
##Passworteingabe-Widgets

###Erstellt einen Button zum Umschalten der Anzeige eines Passwortfelds
####class PasswortShowButton(QPushButton):
    // __init__
    // Nimmt die Argumente:
    //   * config, eine Instantz der Klasse PasswortButtonStrings
    //   * passwort_eingabe, das Eingbaefeld, das durch den Button umgeschaltet werden soll
    //   * shortcut, ist der Shortcut, über den der Button angesteuert werden kann 
    def __init__(self, config: PasswortButtonStrings, passwort_eingabe: PasswortEntry, shortcut=None)
    
    // set_from_config
    // Nimmt das Argument:
    //  * config, vom Typ PasswortPuttonStrings
    // Und setzt die Strings des Widgets auf die Neue Konfiguration
    
    // set
    // Nimmt keine Argumente
    // Und setzt den Wert des Buttons auf gedrückt
    def set(self)
    
    // reset
    // Nimmt keine Argumente
    // Und setzt den Wert des Buttons auf nicht gedrückt
    def reset(self)
    
    // Sonst nur interne Methoden



### Erstellt ein Eingabefeld für Passworte
####class Passwort Entry(QLineEdit):
    // __init__
    // Nimmt die Argumente:
    //   * config, eine Instanz der Klasse PasswortEntryStrings
    //   * onreturn, eine Funktion, die Ausgeführt wird, wenn im Input Feld Enter gedrückt wird
    //   * on_text_changed, eine Funktion, die ausgeführt wird, wenn sich der Text im Feld ändert
    def __init__(self, config: dict, onreturn=None, on_text_changed=None)
    
    // passwort_anzeigen
    // Nimmt keine Argumente
    // Und zeigt den Wert des Passwortfeldes an
    def passwort_anzeigen(self)
    
    // passwort_verstecken
    // Nimmt keine Argumente
    // Und versteckt das Passwort
    def passwort_verstecken(self)
    
    // set_from_config
    // Nimmt das Argument:
    //   * config, eine Instantz der Klasse PasswortEntryStrings
    def set_from_config(self, config: PasswortEntryStrings)
    
    // set
    // Nimmt das Argument text
    // Und Setzt den Wert des Passwortfeldes darauf
    def set(self, text)
    
    // reset
    // Nimmt keine Argumente
    // Und setzt den Wert zurück

------------------------------------------------------------------------------------------------------------------------

####class _EntryLabel(QLabel):
    // __init__
    // Nimmt das Argument:
    //   * config, eine Instantz der Klasse LabelWidget
    def __init__(self, config: LabelWidget)
    
    // set_from_config
    // Nimmt das Argument:
    //   * config, eine Instantz der Klasse LabelWidget
    def set_from_config(self, config: LabelWidget)

------------------------------------------------------------------------------------------------------------------------

### Enthält einen Button zum bestätigen des Passworts
####class _PasswortSubmit(QPuschButton):
    // __init__
    // Nimmt die Argumente:
    //   * config, eine Instatz der Klasse SubmitWidgetStrings zur Konfiguration
    //   * function, eine Funktion, die ausgeführt wird, wenn der Button angeklickt wird
    //   * shortcut, eine Tastenkombi, um den Button anzusteuern
    def __init__(self, config: dict, function, shortcut=None)
    
    // set_from_config
    // Nimmt das Argument:
    //   * config, eine Instantz der Klasse SubmitWidgetStrings zur Konfiguration
    def set_from_config(self, config: dict)
    
    // enable:
    // Nimmt keine Argumente
    // Und macht den Button anklickbar
    def enable(self)
    
    // disable:
    // Nimmt keine Argumente
    // Und sorgt dafür, dass der Button nicht mehr anklickbar ist
    def disable(self)

------------------------------------------------------------------------------------------------------------------------
##Dieses Paket enthaelt Klassen zum Konfigurieren des Eingabefensters

 
####class UserEntryStrings:
    Nimmt die Strings placeholder, whats_this

####class UserWidgetStrings:
    Nimmt die Strings label_text, entry_placeholder, entry_whats_this

------------------------------------------------------------------------------------------------------------------------

####class SubmitWhatsThis:
    Nimmt die Strings not_clickable, clickable

####class SubmitWidgetStrings:
    Nimmt die Strings text, whats_this_not_clickable, whats_this_clickable

------------------------------------------------------------------------------------------------------------------------

####class PasswortEntryStrings:
    Nimmt die Strings placeholder und whats_this

####class PasswortButtonStrings:
    Nimmt den String whats_this

####class PasswortWidgetStrings:
    Nimmt die Strings label_text, entry_placeholder, entry_whats_this, button_whats_this

------------------------------------------------------------------------------------------------------------------------

####class WindowKonfiguration:
    Nimmt den String title
