from PyQt5.QtWidgets import QLabel


__date__ = "09.03.2021"
__status__ = "Production"
__annotations__ = "Wird innerhalb des Pakets verwendet"
__doc__ = """
class _EntryLabel(QLabel):
    # __init__
    # Nimmt das Argument:
    #   * config, ein dictionary der Form
    #   {
    #       "text": "Anzeigetext"
    #   }
    def __init__(self, config: dict)
    
    # set_from_dic
    # Nimmt das Argument:
    #   * config, ein dictionary, der Form
    #   {
    #       "text": "Neuer Anzeigetext"
    #   }
    def set_from_dic(self, config: dict)
"""


class _EntryLabel(QLabel):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, config: dict):
        super(_EntryLabel, self).__init__()
        self.set_from_dic(config)
        pass

    def set_from_dic(self, config: dict):
        """Setzt den Anzeigetext auf den des dics"""
        self.setText(config["text"])
    pass
