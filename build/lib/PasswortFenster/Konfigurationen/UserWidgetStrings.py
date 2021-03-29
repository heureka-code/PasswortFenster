from .LabelKonfiguration import LabelWidget


__doc__ = """
class UserEntryStrings:
    Nimmt die Argumete placeholder, whats_this

class UserWidgetStrings:
    Nimmt die Strings label_text, entry_placeholder, entry_whats_this
"""


class UserEntryStrings:
    def __init__(self, placeholder: str, whats_this: str):
        self.placeholder = placeholder
        self.whats_this = whats_this
        pass
    pass


class UserWidgetStrings:
    def __init__(self,
                 label_text: str,
                 entry_placeholder: str,
                 entry_whats_this: str):
        self.label: LabelWidget = LabelWidget(label_text)
        self.entry: UserEntryStrings = UserEntryStrings(entry_placeholder, entry_whats_this)
        pass
    pass
