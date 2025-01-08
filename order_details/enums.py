from enum import Enum
from django.utils.translation import gettext_lazy as _

class OrderStatus(Enum):
    PENDING    = ("pending",      _("Order has been placed and is awaiting processing."))
    PROCESSING = ("processing",   _("Order is currently being processed."))
    SHIPPED    = ("shipped",      _("Order has been shipped to the customer."))
    DELIVERED  = ("delivered",    _("Order has been delivered to the customer."))
    CANCELLED  = ("cancelled",    _("Order has been cancelled."))
    
    @classmethod
    def choices(cls):
        return [(key.value[0], key.value[1]) for key in cls]