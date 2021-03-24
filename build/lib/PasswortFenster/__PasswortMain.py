from base64 import b64decode
from os import makedirs, getcwd
from os.path import isfile

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout

try:
    from __PasswortEingabeWidget.__PasswortEntry import PasswortEntry as _PasswortEntry
    from __PasswortEingabeWidget.__PasswortShowButton import PasswortShowButton as _PasswortShowButton
    from __EntryLabel import _EntryLabel as _EntryLabel
    from __UserEingabeWidget import UserEntry as _UserEntry
    from __PasswortSubmit import _PasswortSubmit as _PasswortSubmit
except ModuleNotFoundError:
    from PasswortFenster.__PasswortEingabeWidget.__PasswortEntry import PasswortEntry as _PasswortEntry
    from PasswortFenster.__PasswortEingabeWidget.__PasswortShowButton import PasswortShowButton as _PasswortShowButton
    from .__EntryLabel import _EntryLabel as _EntryLabel
    from PasswortFenster.__UserEingabeWidget import UserEntry as _UserEntry
    from .__PasswortSubmit import _PasswortSubmit as _PasswortSubmit

__date__ = "09.03.2021"
__status__ = "Production"
__annotations__ = "Wird innerhalb des Pakets verwendet"
__doc__ = """
# Enthält ein Passwort Fenster zum eingeben von Username und Passwort
class PasswortMainWindow(QWidget):
    # __init__
    # Nimmt die Argumente:
    #   * function, eine Funktion, die ausgeführt wird, wenn bestätigt wird
    #   * config, ein dictionary der Struktur: (default Wert hier angegeben falls None)
    #   {
    #       "title": "Passworteingabe",
    #        "user":
    #           {"label":
    #           {"text": "Username:"},
    #            "entry": 
    #               {
    #                   "placeholder": "Username", 
    #                   "whats_this": "Bitte geben Sie den Usernamen ein"
    #               }
    #         },
    #         "pwd1": {
    #           "label": {"text": "Passwort:"},
    #           "entry": {
    #                       "placeholder": "Passwort", 
    #                       "whats_this": "Passwort eingeben"
    #                    },
    #           "button": {"whats_this": "Passwort anzeigen (Strg + s)"}},
    #          "pwd2": {
    #            "label": {"text": "Passwort wiederholen:"},
    #            "entry": {
    #                           "placeholder": "Passwort wiederholen", 
    #                           "whats_this": "Passwort wiederholen"
    #                     },
    #            "button": {"whats_this": "Passwort anzeigen (Strg + Shift + s)"}},
    #          "submit": {
    #               "text": "Bestätigen",
    #               "whats_this": {
    #                   "not_clickable": "Bitte geben Sie übereinstimmende Passworte ein",
    #                   "clickable": "Passworte Bestätigen (Strg + c)"}}
    #   }
    #   * user_widget, ein bool, der angibt, ob auch ein Fenster zum eingeben des Benutzernamens erstellt werden soll
    #   * passwort_wiederherstellen_widget, ein bool, ob ein Fenster zum wiederholen des Passwortes erstellt werden soll
    def __init__(self, function, config: dict = None, user_widget=True, passwort_wiederholen_widget=True)
    
    # set_from_dic
    # Nimmt das Argument config
    # Und setzt die Einstellungen auf ein dic der oben gezeigten Struktur in __init__
    def set_from_dic(config: dict)
    
    # reset
    # Nimmt keine Argumente
    # Und setzt die Werte aller Widgets zurück
    def reset(self)
"""


class PasswortMainWindow(QWidget):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self, function, config: dict = None, user_widget=True, passwort_wiederholen_widget=True, icon: QIcon=None):
        super(PasswortMainWindow, self).__init__()
        if icon:
            self.setWindowIcon(icon)
        else:
            makedirs(getcwd()+"/data", exist_ok=True)
            if isfile(getcwd()+"/data/show_password.png")==False:
                with open(getcwd()+"/data/show_password.png", "wb") as f_out:
                    f_out.write(b64decode(
                        b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAADEUlEQVR42uxVz0scSRh9X3VVl41IkJFmFkRpfwwInma9LKiB8Q8YEPbUYiCnYU4bWP8K97Lgwu4lC2Jj2IXAHD0oBAZyCC45CFEjztoIEaHRMAzd0z+q9rB27yTLbg4hl5DvVNSh3vu+771XpLXGpyyGT1xfAD5YHAD6/T6klAAApRQY+xu31+s9TJLEvLi4qHY6na9vb2+/MgwjGxsb+3NqaurFxMTES6UUHx4efgwAcRzDNE0Mvklaa2itQUSDwPWTk5P7+/v7jfPzcyvLMhARTNMEYwxKKQAAEaFarb5aWFh46jjOCwCtNE0BAIZhgIj+AYjjGFJKRFHkHhwcNNrt9mIURZBSQmsNpRSUUiAiMMZARMXdyMgIarVaa2lp6VcArUGmlPsgSRIIIepbW1u/XV1dmXEcQ2sNxhhs24bruhulUukSAIIgGPc8b/P6+hpaa3DO0e/3MT09HTYajTXG2NN3lpxlGYQQ9Z2dnR993zd7vV7B1LZtNJvNB+Vy+bUQ4okQ4km5XH7dbDYf2LZddM85h+/71t7e3iMA9XyMuYq+PT09XTw6OprUWsM0TRARtNZwXXfDsqy3Wuuida11y7Kst67rbuQT4JwjjmMcHh4uHh8f3wewWgAYhhFvb29/n8+WiJBlGRhjuBtLa1AEd+dWqVS65JyDc45erwchBIIgwO7u7iPGWFbI9GMqJ2SaJoQQUErBMAy8vwNzfX39B6UUclUZhgGlFIIgGAdQHwzFu3M9CIJxpRSSJIGUEt1uF0IIrK6u/vS+k3+vVCrt+fn5CyJCriAigud5m2EY3iOi+gDrehiG9zzP28zlGoYh0jRFpVJ5Mzc39yyX60fLNMuywr2Tk5PdtbW17yzLepynwQeNJoQouskXPej+KIpgWRaWl5fbKysrP0spvSRJwDl/18n/FRW+71tJkhSLzDNHaw0hBBzH6dZqtV9mZ2fbAFp5lhWktNb/G3ZpmpqdTqd6dnb2zc3NzTgAjI6OXs7MzDx3HOcPKWV3aGjIA4A0TcE5/3fYfflwPm+AvwYA2JLFJZBFdn8AAAAASUVORK5CYII='))
            self.setWindowIcon(QIcon(getcwd() + "/data/show_password.png"))
        if config:
            pass
        else:
            config = {
            "title": "Passworteingabe",
            "user":
                 {"label":
                      {"text": "Username:"},
                  "entry": {"placeholder": "Username", "whats_this": "Bitte geben Sie den Usernamen ein"}},
             "pwd1": {
                 "label": {"text": "Passwort:"},
                 "entry": {"placeholder": "Passwort", "whats_this": "Passwort eingeben"},
                 "button": {"whats_this": "Passwort anzeigen (Strg + s)"}},
             "pwd2": {
                 "label": {"text": "Passwort wiederholen:"},
                 "entry": {"placeholder": "Passwort wiederholen", "whats_this": "Passwort wiederholen"},
                 "button": {"whats_this": "Passwort anzeigen (Strg + Shift + s)"}},
            "submit": {
                "text": "Bestätigen",
                "whats_this": {
                    "not_clickable": "Bitte geben Sie übereinstimmende Passworte ein",
                    "clickable": "Passworte Bestätigen (Strg + c)"}}}
        self.__function = function
        self.setWindowTitle(config["title"])
        self.__user_widget = user_widget
        self.__passwort_wiederholen_widget = passwort_wiederholen_widget
        if user_widget:
            user_label = _EntryLabel(config["user"]["label"])
            self.__user_entry = _UserEntry(config["user"]["entry"], on_text_changed=self.__gleich_heits_pruefer)

        pwd_label = _EntryLabel(config["pwd1"]["label"])
        self.__pwd_entry = _PasswortEntry(config["pwd1"]["entry"], on_text_changed=self.__gleich_heits_pruefer)
        self.__pwd_show = _PasswortShowButton(config["pwd1"]["button"], self.__pwd_entry, shortcut="ctrl+s", icon=icon)

        if passwort_wiederholen_widget:
            pwd2_label = _EntryLabel(config["pwd2"]["label"])
            self.__pwd2_entry = _PasswortEntry(config["pwd2"]["entry"], on_text_changed=self.__gleich_heits_pruefer)
            self.__pwd2_show = _PasswortShowButton(config["pwd2"]["button"], self.__pwd2_entry, shortcut="ctrl+shift+s",
                                                   icon=icon)

        self.__submit = _PasswortSubmit(config["submit"], self.__on_submit, shortcut="ctrl+c")

        entryBox = QGridLayout()
        if user_widget:
            start = 1
            entryBox.addWidget(user_label, 0, 0)
        else:
            start = 0
        entryBox.addWidget(pwd_label, start, 0)
        if passwort_wiederholen_widget:
            entryBox.addWidget(pwd2_label, start+1, 0)

        if user_widget:
            entryBox.addWidget(self.__user_entry, 0, 1)
        entryBox.addWidget(self.__pwd_entry, start, 1)
        if passwort_wiederholen_widget:
            entryBox.addWidget(self.__pwd2_entry, start + 1, 1)

        entryBox.addWidget(self.__pwd_show, start, 2)
        if passwort_wiederholen_widget:
            entryBox.addWidget(self.__pwd2_show, start + 1, 2)

        inneres_layout = QVBoxLayout()
        inneres_layout.addLayout(entryBox)
        inneres_layout.addWidget(self.__submit)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addLayout(inneres_layout)
        layout.addStretch(1)

        self.setLayout(layout)
        self.show()
        pass

    def __on_submit(self):
        """Wird ausgeführt, wenn der Submit-Button gedrücktwird und leitet die Eingaben in Form function(Username, Passwort),
wobei Username immer None ist, wenn kein dafür ausgelegtes Feld gewünscht ist"""
        if self.__user_widget:
            user = self.__user_entry.text()
        else:
            user = None
        if self.__passwort_wiederholen_widget:
            if self.__pwd_entry.text() == self.__pwd2_entry.text():
                self.__function(user, self.__pwd_entry.text())
        else:
            self.__function(user, self.__pwd_entry.text())
        pass

    def __gleich_heits_pruefer(self, x=None):
        """Wird ausgeführt, wenn der Inhalt der Felder verändert wird und Prüft, ob der Button noch anklickbar sein soll"""
        self.__submit.enable()
        if self.__user_widget:
            if self.__user_entry.text() == "":
                self.__submit.disable()
        if self.__pwd_entry.text() == "":
            self.__submit.disable()
        if self.__passwort_wiederholen_widget:
            if self.__pwd2_entry.text() == "" or self.__pwd_entry.text() != self.__pwd2_entry.text():
                self.__submit.disable()
        pass

    def set_from_dic(self, config: dict):
        """Setzt die Strings des Widgets nach dem dictionary"""
        self.__pwd_entry.set_from_dic(config["pwd1"])
        if self.__passwort_wiederholen_widget:
            self.__pwd2_entry.set_from_dic(config["pwd2"])
        if self.__user_widget:
            self.__user_entry.set_from_dic(config["user"])
        if "title" in config.keys():
            self.setWindowTitle(config["title"])
        pass

    def reset(self):
        if self.__user_widget:
            self.__user_entry.reset()
        self.__pwd_entry.reset()
        self.__pwd_show.reset()
        if self.__passwort_wiederholen_widget:
            self.__pwd2_entry.reset()
            self.__pwd2_show.reset()
        self.__gleich_heits_pruefer()
    pass
