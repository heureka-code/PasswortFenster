from os import getcwd

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

try:
    from __PasswortEntry import PasswortEntry
except ModuleNotFoundError:
    from .__PasswortEntry import PasswortEntry


__date__ = "09.03.2021"
__status__ = "Production"
__doc__ = """
Erstellt einen Button zum Umschalten der Anzeige eines Passwortfelds
class PasswortShowButton(QPushButton):
    # __init__
    # Nimmt die Argumente:
    #   * config, ein dictionary der Form:
    #   {
    #       "whats_this": "Tool Tip"
    #   }
    #   * passwort_eingabe, das Eingbaefeld, das durch den Button umgeschaltet werden soll
    #   * shortcut, ist der Shortcut, über den der Button angesteuert werden kann 
    def __init__(self, config: dict, passwort_eingabe: PasswortEntry, shortcut=None)
    
    # set_from_dic
    # Nimmt das Argument:
    #   * config, ein dictionary der Form:
    #   {
    #       "whats_this": "Neuer Tool Tip"
    #   }
    def set_from_dic(self, config: dict)
    
    # set
    # Nimmt keine Argumente
    # Und setzt den Wert des Buttons auf gedrückt
    def set(self)
    
    # reset
    # Nimmt keine Argumente
    # Und setzt den Wert des Buttons auf nicht gedrückt
    def reset(self)
"""
__annotations__ = "Wird innerhalb des Pakets verwendet"


class PasswortShowButton(QPushButton):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: dict, passwort_eingabe: PasswortEntry, shortcut=None, icon:QIcon=None):
        super(PasswortShowButton, self).__init__()
        self.__passwort_eingabe = passwort_eingabe
        self.set_from_dic(config)
        self.setCheckable(True)
        if icon:
            self.setIcon(icon)
        else:
            self.setIcon(QIcon(getcwd()+"/data/show_password.png"))
        if shortcut:
            self.setShortcut(shortcut)
        self.clicked.connect(self.__state_changed)
        pass

    def __state_changed(self):
        """Wird ausgeführt, wenn der Button seinen Status durch klicken verändert und Prüft, ob das zugehörige Passwort angezeigt werden soll"""
        if self.isChecked():
            self.__passwort_eingabe.passwort_anzeigen()
        else:
            self.__passwort_eingabe.passwort_verstecken()
        pass

    def set_from_dic(self, config: dict):
        """Setzt die Strings des Widgets auf die des dictionary"""
        self.setToolTip(config["whats_this"])
        self.setWhatsThis(config["whats_this"])
        pass

    def set(self):
        self.setChecked(True)
        self.__state_changed()

    def reset(self):
        self.setChecked(False)
        self.__state_changed()
    pass
