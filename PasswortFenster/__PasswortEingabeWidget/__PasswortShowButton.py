from os import getcwd

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

try:
    from __PasswortEntry import PasswortEntry
except ModuleNotFoundError:
    from .__PasswortEntry import PasswortEntry
from ..Konfigurationen.PasswortWidgetStrings import PasswortButtonStrings


__date__ = "29.03.2021"
__status__ = "Production"
__doc__ = """
Erstellt einen Button zum Umschalten der Anzeige eines Passwortfelds
class PasswortShowButton(QPushButton):
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
"""
__annotations__ = "Wird innerhalb des Pakets verwendet"


class PasswortShowButton(QPushButton):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self,
                 config: PasswortButtonStrings,
                 passwort_eingabe: PasswortEntry,
                 shortcut=None,
                 icon: QIcon = None):
        super(PasswortShowButton, self).__init__()
        self.__passwort_eingabe: PasswortEntry = passwort_eingabe
        self.set_from_config(config)
        self.setCheckable(True)
        if icon:
            self.setIcon(icon)
        else:
            self.setIcon(QIcon(getcwd()+"/data/show_password.png"))
        if shortcut:
            self.setShortcut(shortcut)
        self.clicked.connect(self.__state_changed)
        pass

    def set_from_config(self, config: PasswortButtonStrings):
        """Setzt die Strings des Widgets auf die des dictionary"""
        self.setToolTip(config.whats_this)
        self.setWhatsThis(config.whats_this)
        pass

    def set(self):
        self.setChecked(True)
        self.__state_changed()
        pass

    def reset(self):
        self.setChecked(False)
        self.__state_changed()
        pass

    def __state_changed(self):
        """Wird ausgeführt, wenn der Button seinen Status durch klicken verändert und Prüft, ob das zugehörige Passwort angezeigt werden soll"""
        if self.isChecked():
            self.__passwort_eingabe.passwort_anzeigen()
        else:
            self.__passwort_eingabe.passwort_verstecken()
        pass
    pass
