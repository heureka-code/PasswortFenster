from PyQt5.QtWidgets import QLineEdit

from ..Konfigurationen.UserWidgetStrings import UserEntryStrings


__date__ = "29.03.2021"
__status__ = "Production"
__annotations__ = "Am besten für die Verendung innerhalb des Pakets geeignet"
__doc__ = """
// Erstellt ein Eingabefeld für einen Benutzernamen
class __UserEingabeWidget(QLineEdit):
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
"""


class UserEntry(QLineEdit):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: UserEntryStrings = None, onreturn=None, on_text_changed=None):
        super(UserEntry, self).__init__()
        self.set_from_config(config)
        if on_text_changed:
            self.textChanged.connect(on_text_changed)
        if onreturn:
            self.returnPressed.connect(onreturn)
        pass

    def set_from_config(self, config: UserEntryStrings):
        """Setzt die Strings des Widgets auf das gegebene dictionary"""
        self.setPlaceholderText(config.placeholder)
        self.setWhatsThis(config.whats_this)
        self.setToolTip(config.whats_this)
        pass

    def reset(self):
        self.set("")
        pass

    def set(self, text):
        self.setText(text)
    pass
