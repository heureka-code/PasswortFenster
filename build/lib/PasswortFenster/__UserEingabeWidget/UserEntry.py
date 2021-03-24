from PyQt5.QtWidgets import QLineEdit


__date__ = "09.03.2021"
__status__ = "Production"
__annotations__ = "Am besten für die Verendung innerhalb des Pakets geeignet"
__doc__ = """
# Erstellt ein Eingabefeld für einen Benutzernamen
class __UserEingabeWidget(QLineEdit):
    # __init__
    # Nimmt die Argumente:
    #   * confi, ein dictionary der Struktur:
    #   {
    #       "placeholder": "Platzhalter für das Eingbaefeld",
    #       "whats_this": "Tool Tip, der beim hovern angezeigt wird"
    #   }
    #   * onreturn, eine Funktion, die ausgeführt wird, wenn im Feld Enter gedrückt wird
    #   * on_text_changed, eine Funktion, die Ausgeführt wird, wenn sich der Text des Feldes ändert
    def __init__(self, config: dict, onreturn=None, on_text_changed=None)
    
    # set_from_dic
    # Nimmt das Argument:
    #   * config, ein dictionary der Form:
    #   {
    #       "placeholder": "Der Platzhalter im Eingabefeld",
    #       "whats_this": "Der Tool Tip, der beim hovern angezeigt wird",
    #   }
    def set_from_dic(config: dict)
    
    # reset
    # Nimmt keine Argumente
    # Und setzt den Text zurück
    def reset(self)
    
    # set
    # Nimmt das Argument text
    # Und setzt den Wert des Feldes darauf
    def set(self, text)
"""


class UserEntry(QLineEdit):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: dict =None, onreturn=None, on_text_changed=None):
        super(UserEntry, self).__init__()
        if config:
            self.__config = config
        else:
            self.__config = {"placeholder": "Username", "whats_this": "Bitte geben Sie den Usernamen ein"}
        self.set_from_dic(self.__config)
        if on_text_changed:
            self.textChanged.connect(on_text_changed)
        if onreturn:
            self.returnPressed.connect(onreturn)
        pass

    def set_from_dic(self, config: dict):
        """Setzt die Strings des Widgets auf das gegebene dictionary"""
        self.setPlaceholderText(config["placeholder"])
        self.setWhatsThis(config["whats_this"])
        self.setToolTip(config["whats_this"])
        pass

    def reset(self):
        self.set("")
        pass

    def set(self, text):
        self.setText(text)
    pass
