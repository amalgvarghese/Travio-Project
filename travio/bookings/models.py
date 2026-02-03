# from django.db import models

# # Create your models here.
# from django.conf import settings
# from packages.models import Package
# import uuid

# class Booking(models.Model):

#     uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

#     STATUS_CHOICES = (
#         ("booked", "Booked"),
#         ("cancelled", "Cancelled"),
#     )

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     package = models.ForeignKey(Package, on_delete=models.CASCADE)

#     start_date = models.DateField()

#     total_amount = models.FloatField()


#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="booked")

#     created_at = models.DateTimeField(auto_now_add=True)

#     is_paid = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.user} - {self.package.name}"
