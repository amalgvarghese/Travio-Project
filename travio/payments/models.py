from django.db import models
from django.conf import settings
from packages.models import Package
import uuid


class Payment(models.Model):

    PAYMENT_STATUS = (
        ("created", "Created"),
        ("success", "Success"),
        ("failed", "Failed"),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="created"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.package} - {self.status}"
