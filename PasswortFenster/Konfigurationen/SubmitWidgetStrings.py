__doc__ = """
class SubmitWhatsThis:
    Nimmt die Strings not_clickable, clickable

class SubmitWidgetStrings:
    Nimmt die Strings text, whats_this_not_clickable, whats_this_clickable
"""


class SubmitWhatsThis:
    def __init__(self, not_clickable: str, clickable: str):
        self.not_clickable = not_clickable
        self.clickable = clickable
        pass
    pass


class SubmitWidgetStrings:
    def __init__(self,
                 text: str,
                 whats_this_not_clickable: str,
                 whats_this_clickable: str):
        self.text = text
        self.whats_this = SubmitWhatsThis(whats_this_not_clickable,
                                          whats_this_clickable)
        pass
    pass
