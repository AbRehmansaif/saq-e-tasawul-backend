from enum import Enum
from django.utils.translation import gettext_lazy as _

class PaymentStatus(Enum):
    PENDING = ("pending", _("Payment is yet to be completed."))
    COMPLETE = ("complete", _("Payment has been successfully completed."))
    FAILED = ("failed", _("Payment was unsuccessful."))
    REFUNDED = ("refunded", _("Payment has been refunded to the customer."))

    @classmethod
    def choices(cls):
        return [(key.value[0], key.value[1]) for key in cls]
