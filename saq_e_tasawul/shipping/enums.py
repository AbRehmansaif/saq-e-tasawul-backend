from enum import Enum
from django.utils.translation import gettext_lazy as _


class ShippingMethod(Enum):
    STANDARD      = ("standard",      _("Standard shipping (3-5 business days)."))
    EXPRESS       = ("express",       _("Express shipping (1-2 business days)."))
    OVERNIGHT     = ("overnight",     _("Overnight shipping (next-day delivery)."))
    INTERNATIONAL = ("international", _("International shipping (varies by destination)."))
    PICKUP        = ("pickup",        _("Pickup from store or warehouse."))