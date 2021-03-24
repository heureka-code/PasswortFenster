from PyQt5.QtWidgets import QPushButton


__date__ = "09.03.2021"
__status__ = "Production"
__annotations__ = "Wird innerhalb des Pakets verwendet"
__doc__ = """
# Enthält einen Button zum bestätigen des Passworts
class _PasswortSubmit(QPuschButton):
    # __init__
    # Nimmt die Argumente:
    #   * config, ein dictionary, def Form
    #   {
    #       "text": "Buttontext",
    #       "whats_this":
    #           {
    #               "not_clickable": "Tool Tip, wenn der Button nicht anklickbar ist",
    #               "clickable": "Tool Tip, wenn der Button anklickbar ist"
    #           }
    #   }
    #   * function, eine Funktion, die ausgeführt wird, wenn der Button angeklickt wird
    #   * shortcut, eine Tastenkombi, um den Button anzusteuern
    def __init__(self, config: dict, function, shortcut=None)
    
    # set_from_dic
    # Nimmt das Argument:
    #   * config, ein dictionary, def Form
    #   {
    #       "text": "Neuer Buttontext",
    #       "whats_this":
    #           {
    #               "not_clickable": "Neuer Tool Tip, wenn der Button nicht anklickbar ist",
    #               "clickable": "Neuer Tool Tip, wenn der Button anklickbar ist"
    #           }
    #   }
    def set_from_dic(self, config: dict)
    
    # enable:
    # Nimmt keine Argumente
    # Und macht den Button anklickbar
    def enable(self)
    
    # disable:
    # Nimmt keine Argumente
    # Und sorgt dafür, dass der Button nicht mehr anklickbar ist
"""


class _PasswortSubmit(QPushButton):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: dict, function, shortcut=None):
        super(_PasswortSubmit, self).__init__()
        self.__config = config
        self.set_from_dic(config)
        if shortcut:
            self.setShortcut(shortcut)
        self.clicked.connect(function)
        self.disable()
        pass

    def set_from_dic(self, config: dict):
        """Setzt die Strings des Widgets auf das gegebene dictionary"""
        self.setText(config["text"])
        self.setWhatsThis(config["whats_this"]["clickable" if self.isEnabled() else "not_clickable"])
        self.setToolTip(config["whats_this"]["clickable" if self.isEnabled() else "not_clickable"])
        pass

    def enable(self):
        """Macht den Button anklickbar"""
        self.setEnabled(True)
        self.set_from_dic(self.__config)
        pass

    def disable(self):
        """Macht den Button nich-anklickbar"""
        self.setEnabled(False)
        self.set_from_dic(self.__config)
    pass
