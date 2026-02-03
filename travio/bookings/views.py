# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib import messages
# from .models import Booking
# from packages.models import Package
# from .forms import BookingForm
# from datetime import date
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# # Show all bookings of the logged-in user
# class BookingsView(View):
#     template = "bookings/my-bookings.html"

#     def get(self, request):
#         bookings = Booking.objects.filter(user=request.user).order_by("-created_at")
#         return render(request, self.template, {"bookings": bookings})


# # Create a new package booking
# @method_decorator(login_required(login_url='must-login'), name='dispatch')
# class BookingCreateView(View):
#     template_name = "bookings/booking-create.html"

#     def get(self, request, uuid):
#         package = Package.objects.get(uuid=uuid)
#         form = BookingForm()
#         return render(request, self.template_name, {"package": package, "form": form})

#     def post(self, request, uuid):
#         package = Package.objects.get(uuid=uuid)
#         form = BookingForm(request.POST)

#         if form.is_valid():
#             start_date = form.cleaned_data["start_date"]
#             today = date.today()

#             # Prevent past dates
#             if start_date < today:
#                 messages.warning(request, "You cannot select past dates")
#                 return redirect("booking-create", uuid=uuid)

#             # Check if package is already booked on that date
#             booked = Booking.objects.filter(
#                 package=package,
#                 start_date=start_date,
#                 status="booked"
#             ).exists()

#             if booked:
#                 messages.warning(request, "This package is already booked on this date")
#                 return redirect("booking-create", uuid=uuid)

#             # Calculate total amount (assuming package has a price field)
#             total_amount = package.price

#             # Create the booking
#             Booking.objects.create(
#                 user=request.user,
#                 package=package,
#                 start_date=start_date,
#                 total_amount=total_amount,
#                 status="booked"
#             )

#             messages.success(request, "Booking created successfully")
#             return redirect("my-bookings")

#         return render(request, self.template_name, {"package": package, "form": form})


# # Booking detail view
# class BookingDetailView(View):
#     template_name = "bookings/booking-details.html"

#     def get(self, request, uuid):
#         booking = Booking.objects.filter(uuid=uuid, user=request.user).first()
#         if not booking:
#             messages.error(request, "Booking not found")
#             return redirect("my-bookings")
#         return render(request, self.template_name, {"booking": booking})


# # Cancel a booking
# class BookingCancelView(View):
#     def get(self, request, uuid):
#         booking = Booking.objects.filter(uuid=uuid, user=request.user).first()
#         if not booking:
#             messages.error(request, "Invalid booking")
#             return redirect("my-bookings")

#         booking.status = "cancelled"
#         booking.save()
#         messages.success(request, "Booking Cancelled")
#         return redirect("my-bookings")
