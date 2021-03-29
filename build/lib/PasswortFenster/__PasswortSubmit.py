from PyQt5.QtWidgets import QPushButton

from .Konfigurationen import SubmitWidgetStrings

__date__ = "09.03.2021"
__status__ = "Production"
__annotations__ = "Wird innerhalb des Pakets verwendet"
__doc__ = """
# Enthält einen Button zum bestätigen des Passworts
class _PasswortSubmit(QPuschButton):
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
"""


class _PasswortSubmit(QPushButton):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: SubmitWidgetStrings, function, shortcut=None):
        super(_PasswortSubmit, self).__init__()
        self.__config: SubmitWidgetStrings = config
        self.set_from_config(config)
        if shortcut:
            self.setShortcut(shortcut)
        self.clicked.connect(function)
        self.disable()
        pass

    def set_from_config(self, config: SubmitWidgetStrings):
        """Setzt die Strings des Widgets auf das gegebene dictionary"""
        self.setText(config.text)
        self.setWhatsThis(config.whats_this.clickable if self.isEnabled() else config.whats_this.not_clickable)
        self.setToolTip(config.whats_this.clickable if self.isEnabled() else config.whats_this.not_clickable)
        pass

    def enable(self):
        """Macht den Button anklickbar"""
        self.setEnabled(True)
        self.set_from_config(self.__config)
        pass

    def disable(self):
        """Macht den Button nich-anklickbar"""
        self.setEnabled(False)
        self.set_from_config(self.__config)
    pass
