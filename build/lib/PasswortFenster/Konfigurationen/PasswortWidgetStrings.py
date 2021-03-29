from .LabelKonfiguration import LabelWidget


__doc__ = """
class PasswortEntryStrings:
    Nimmt die Strings placeholder und whats_this

class PasswortButtonStrings:
    Nimmt den String whats_this

class PasswortWidgetStrings:
    Nimmt die Strings label_text, entry_placeholder, entry_whats_this, button_whats_this
"""


class PasswortEntryStrings:
    def __init__(self, placeholder: str, whats_this: str):
        self.placeholder = placeholder
        self.whats_this = whats_this
        pass
    pass


class PasswortButtonStrings:
    def __init__(self, whats_this: str):
        self.whats_this = whats_this
        pass
    pass


class PasswortWidgetStrings:
    def __init__(self,
                 label_text: str,
                 entry_placeholder: str,
                 enty_whats_this: str,
                 button_whats_this: str):
        self.label: LabelWidget = LabelWidget(label_text)
        self.entry: PasswortEntryStrings = PasswortEntryStrings(entry_placeholder, enty_whats_this)
        self.button: PasswortButtonStrings = PasswortButtonStrings(button_whats_this)
        pass
    pass
