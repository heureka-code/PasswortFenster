from PyQt5.QtWidgets import QLabel
from .Konfigurationen.LabelKonfiguration import LabelWidget


__date__ = "29.03.2021"
__status__ = "Production"
__annotations__ = "Wird innerhalb des Pakets verwendet"
__doc__ = """
class _EntryLabel(QLabel):
    # __init__
    # Nimmt das Argument:
    #   * config, eine Instantz der Klasse LabelWidget
    def __init__(self, config: LabelWidget)
    
    # set_from_config
    # Nimmt das Argument:
    #   * config, eine Instantz der Klasse LabelWidget
    def set_from_config(self, config: LabelWidget)
"""


class _EntryLabel(QLabel):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: LabelWidget):
        super(_EntryLabel, self).__init__()
        self.set_from_config(config)
        pass

    def set_from_config(self, config: LabelWidget):
        """Setzt den Anzeigetext auf den des dics"""
        self.setText(config.text)
    pass
