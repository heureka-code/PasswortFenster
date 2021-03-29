from .UserWidgetStrings import UserWidgetStrings
from .SubmitWidgetStrings import SubmitWidgetStrings
from .PasswortWidgetStrings import PasswortWidgetStrings
from .WindowKonfigurationen import WindowKonfiguration
from .UserWidgetStrings import __doc__ as UserWidgetStrings__doc__
from .SubmitWidgetStrings import __doc__ as SubmitWidgetStrings__doc__
from .PasswortWidgetStrings import __doc__ as PasswortWidgetStrings__doc__
from .WindowKonfigurationen import __doc__ as WindowKonfigurationen__doc__

__doc__ = f"Dieses Paket enthaelt Klassen zum Konfigurieren des Eingabefensters\n\n " +\
          f'\n{"-" * 120}\n'.join([
              UserWidgetStrings__doc__,
              SubmitWidgetStrings__doc__,
              PasswortWidgetStrings__doc__,
              WindowKonfigurationen__doc__])

