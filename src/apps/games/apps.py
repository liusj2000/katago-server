from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GamesConfig(AppConfig):
    """
    Katago Games app handle games submitted by user, whether they are training games (used by training loop)
    or rating games (used to estimate network strength).
    """

    name = "src.apps.games"
    verbose_name = _("Games")

    def ready(self):
        try:
            import src.apps.games.signals  # noqa F401
        except ImportError:
            pass
