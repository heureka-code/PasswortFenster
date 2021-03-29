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
    from Konfigurationen import *
except ModuleNotFoundError:
    from PasswortFenster.__PasswortEingabeWidget.__PasswortEntry import PasswortEntry as _PasswortEntry
    from PasswortFenster.__PasswortEingabeWidget.__PasswortShowButton import PasswortShowButton as _PasswortShowButton
    from .__EntryLabel import _EntryLabel as _EntryLabel, _EntryLabel
    from PasswortFenster.__UserEingabeWidget import UserEntry as _UserEntry
    from .__PasswortSubmit import _PasswortSubmit as _PasswortSubmit
    from .Konfigurationen import *

__date__ = "09.03.2021"
__status__ = "Production"
__annotations__ = "Wird innerhalb des Pakets verwendet"
__doc__ = """
# Enthält ein Passwort Fenster zum eingeben von Username und Passwort
class PasswortMainWindow(QWidget):
    // __init__
    // Nimmt die Argumente:
    //   * function, eine Funktion, die ausgeführt wird, wenn bestätigt wird
    //   * window_konfiguration, eine Instantz der Klasse WindowKonfiguration, mit der die generellen Einstellungen zum Fenster gemacht werden
    //   * submit_widget, eine Instantz der Klasse SubmitWidgetStrings, mit der der Submit Button eingestellt wird
    //   * user_widget, falls gesetzt eine Instantz der Klasse UserWidgetStrings, zur Konfiguration, falls nicht gesetzt wird kein User Widget erstellt
    //   * passwort_widget, eine Instantz der Klasse PasswortWidgetStrings, erstellt falls gesetzt ein Passwort Widget
    //   * passwort_wiederholen_widget, eine Instantz der Klasse PasswortWidgetStrings, erstellt falls gesetzt ein zweites Passwort Widget
    def __init__(self,
                 function,
                 window_konfiguration: WindowKonfiguration,
                 submit_widget: SubmitWidgetStrings,
                 user_widget: UserWidgetStrings = None,
                 passwort_widget: PasswortWidgetStrings = None,
                 passwort_wiederholen_widget: PasswortWidgetStrings = None,
                 icon: QIcon = None,
                 minimum_width: int = None,
                 minimum_height: int = None)
    
    // reset
    // Nimmt keine Argumente
    // Und setzt die Werte aller Widgets zurück
    def reset(self)
"""


class PasswortMainWindow(QWidget):
    __doc__ = __doc__
    __annotations__ = __annotations__

    def __init__(self,
                 function,
                 window_konfiguration: WindowKonfiguration,
                 submit_widget: SubmitWidgetStrings,
                 user_widget: UserWidgetStrings = None,
                 passwort_widget: PasswortWidgetStrings = None,
                 passwort_wiederholen_widget: PasswortWidgetStrings = None,
                 icon: QIcon = None,
                 minimum_width: int = None,
                 minimum_height: int = None):
        super(PasswortMainWindow, self).__init__()
        if minimum_width:
            self.setMinimumWidth(minimum_width)
        if minimum_height:
            self.setMinimumHeight(minimum_height)
        if passwort_wiederholen_widget and (passwort_widget is None):
            passwort_widget = passwort_wiederholen_widget
            passwort_wiederholen_widget = None
        if window_konfiguration is None:
            window_konfiguration = WindowKonfiguration("Passwort Fenster")
        if icon:
            self.setWindowIcon(icon)
        else:
            makedirs(getcwd()+"/data", exist_ok=True)
            if isfile(getcwd()+"/data/show_password.png") is False:
                with open(getcwd()+"/data/show_password.png", "wb") as f_out:
                    f_out.write(b64decode(
                        b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGOfPtRkwAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAADEUlEQVR42uxVz0scSRh9X3VVl41IkJFmFkRpfwwInma9LKiB8Q8YEPbUYiCnYU4bWP8K97Lgwu4lC2Jj2IXAHD0oBAZyCC45CFEjztoIEaHRMAzd0z+q9rB27yTLbg4hl5DvVNSh3vu+771XpLXGpyyGT1xfAD5YHAD6/T6klAAApRQY+xu31+s9TJLEvLi4qHY6na9vb2+/MgwjGxsb+3NqaurFxMTES6UUHx4efgwAcRzDNE0Mvklaa2itQUSDwPWTk5P7+/v7jfPzcyvLMhARTNMEYwxKKQAAEaFarb5aWFh46jjOCwCtNE0BAIZhgIj+AYjjGFJKRFHkHhwcNNrt9mIURZBSQmsNpRSUUiAiMMZARMXdyMgIarVaa2lp6VcArUGmlPsgSRIIIepbW1u/XV1dmXEcQ2sNxhhs24bruhulUukSAIIgGPc8b/P6+hpaa3DO0e/3MT09HTYajTXG2NN3lpxlGYQQ9Z2dnR993zd7vV7B1LZtNJvNB+Vy+bUQ4okQ4km5XH7dbDYf2LZddM85h+/71t7e3iMA9XyMuYq+PT09XTw6OprUWsM0TRARtNZwXXfDsqy3Wuuida11y7Kst67rbuQT4JwjjmMcHh4uHh8f3wewWgAYhhFvb29/n8+WiJBlGRhjuBtLa1AEd+dWqVS65JyDc45erwchBIIgwO7u7iPGWFbI9GMqJ2SaJoQQUErBMAy8vwNzfX39B6UUclUZhgGlFIIgGAdQHwzFu3M9CIJxpRSSJIGUEt1uF0IIrK6u/vS+k3+vVCrt+fn5CyJCriAigud5m2EY3iOi+gDrehiG9zzP28zlGoYh0jRFpVJ5Mzc39yyX60fLNMuywr2Tk5PdtbW17yzLepynwQeNJoQouskXPej+KIpgWRaWl5fbKysrP0spvSRJwDl/18n/FRW+71tJkhSLzDNHaw0hBBzH6dZqtV9mZ2fbAFp5lhWktNb/G3ZpmpqdTqd6dnb2zc3NzTgAjI6OXs7MzDx3HOcPKWV3aGjIA4A0TcE5/3fYfflwPm+AvwYA2JLFJZBFdn8AAAAASUVORK5CYII='))
            self.setWindowIcon(QIcon(getcwd() + "/data/show_password.png"))

        self.__function = function
        self.setWindowTitle(window_konfiguration.title)
        if user_widget:
            user_label: _EntryLabel = _EntryLabel(user_widget.label)
            self.__user_entry = _UserEntry(user_widget.entry,
                                           on_text_changed=self.__gleich_heits_pruefer,
                                           onreturn=self.__on_submit)
        else:
            self.__user_entry = None

        if passwort_widget:
            pwd_label = _EntryLabel(passwort_widget.label)
            self.__pwd_entry = _PasswortEntry(passwort_widget.entry,
                                              on_text_changed=self.__gleich_heits_pruefer,
                                              onreturn=self.__on_submit)
            self.__pwd_show = _PasswortShowButton(passwort_widget.button, self.__pwd_entry,
                                                  shortcut="ctrl+s", icon=icon)

        if passwort_wiederholen_widget:
            pwd2_label = _EntryLabel(passwort_wiederholen_widget.label)
            self.__pwd2_entry = _PasswortEntry(passwort_wiederholen_widget.entry,
                                               on_text_changed=self.__gleich_heits_pruefer,
                                               onreturn=self.__on_submit)
            self.__pwd2_show = _PasswortShowButton(passwort_wiederholen_widget.button, self.__pwd2_entry,
                                                   shortcut="ctrl+shift+s", icon=icon)
        else:
            self.__pwd2_entry = None

        self.__submit = _PasswortSubmit(submit_widget, self.__on_submit, shortcut="ctrl+c")

        entryBox = QGridLayout()
        if user_widget:
            start = 1
            if "" != user_label.text():
                entryBox.addWidget(user_label, 0, 0)
        else:
            start = 0
        if passwort_widget:
            if pwd_label.text() != "":
                entryBox.addWidget(pwd_label, start, 0)
        if passwort_wiederholen_widget:
            if pwd2_label.text() != "":
                entryBox.addWidget(pwd2_label, start+1, 0)

        if user_widget:
            entryBox.addWidget(self.__user_entry, 0, 1)
        if passwort_widget:
            entryBox.addWidget(self.__pwd_entry, start, 1)
        if passwort_wiederholen_widget:
            entryBox.addWidget(self.__pwd2_entry, start + 1, 1)
        if passwort_widget:
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
        if self.__user_entry:
            user = self.__user_entry.text()
        else:
            user = None

        if self.__pwd2_entry and self.__pwd_entry:
            if self.__pwd_entry.text() == self.__pwd2_entry.text():
                if user:
                    self.__function(user, self.__pwd_entry.text())
                else:
                    self.__function(self.__pwd_entry.text())
        elif self.__pwd_entry:
            if user:
                self.__function(user, self.__pwd_entry.text())
            else:
                self.__function(self.__pwd_entry.text())
        else:
            self.__function(user)
        pass

    def __gleich_heits_pruefer(self, *args):
        """Wird ausgeführt, wenn der Inhalt der Felder verändert wird und Prüft, ob der Button noch anklickbar sein soll"""
        self.__submit.enable()
        if self.__user_entry:
            if self.__user_entry.text() == "":
                self.__submit.disable()
        if self.__pwd_entry:
            if self.__pwd_entry.text() == "":
                self.__submit.disable()
        if self.__pwd2_entry:
            if self.__pwd2_entry.text() == "" or self.__pwd_entry.text() != self.__pwd2_entry.text():
                self.__submit.disable()
        pass

    def reset(self):
        if self.__user_widget:
            self.__user_entry.reset()
        if self.__pwd_entry:
            self.__pwd_entry.reset()
            self.__pwd_show.reset()
        if self.__pwd2_entry:
            self.__pwd2_entry.reset()
            self.__pwd2_show.reset()
        self.__gleich_heits_pruefer()
    pass
