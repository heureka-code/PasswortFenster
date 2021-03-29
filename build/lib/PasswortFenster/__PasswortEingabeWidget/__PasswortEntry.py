from PyQt5.QtWidgets import QLineEdit

from ..Konfigurationen.PasswortWidgetStrings import PasswortEntryStrings

__date__ = "29.03.2021"
__status__ = "Production"
__doc__ = """
// Erstellt ein Eingabefeld für Passworte
class Passwort Entry(QLineEdit):
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
"""
__annotations__ = "Am besten für die Verendung innerhalb des Pakets geeignet"


class PasswortEntry(QLineEdit):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: PasswortEntryStrings, onreturn=None, on_text_changed=None):
        super(PasswortEntry, self).__init__()
        self.set_from_dic(config)
        self.passwort_verstecken()
        if on_text_changed:
            self.textChanged.connect(on_text_changed)
        if onreturn:
            self.returnPressed.connect(onreturn)
        pass

    def passwort_anzeigen(self):
        """Zeigt das Passwort im Feld an (Zeichendarstellung)"""
        self.setEchoMode(QLineEdit.Normal)
        pass

    def passwort_verstecken(self):
        """Versteckt das Passwort (Punktdarstellung)"""
        self.setEchoMode(QLineEdit.Password)
        pass

    def set_from_dic(self, config: PasswortEntryStrings):
        """Setzt die Strings auf das gegebene dictionary"""
        self.setPlaceholderText(config.placeholder)
        self.setWhatsThis(config.whats_this)
        self.setToolTip(config.whats_this)
        pass

    def reset(self):
        self.set("")

    def set(self, text):
        self.setText(text)
    pass
