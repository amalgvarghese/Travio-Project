from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from authentication.permissions import permitted_user_roles
from packages.models import Package
import razorpay
from decouple import config

def payment_success(request):
    package_uuid = request.session.get('package_uuid')
    package = None

    if package_uuid:
        package = Package.objects.filter(uuid=package_uuid).first()
        if package:
            package.payment_status = 'paid'
            package.save()

    return render(request, 'payments/payment_success.html', {
        'package': package
    })



def payment_failed(request):
    return render(request, 'payments/payment_failed.html')


@method_decorator(permitted_user_roles(['User']), name='dispatch')
class RazorPayView(View):
    template = 'payments/razorpay.html'

    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')

        package = Package.objects.filter(uuid=uuid).first()
        if not package:
            return redirect('payment_failed') 

        client = razorpay.Client(
            auth=(config("RZP_CLIENT_ID"), config("RZP_CLIENT_SECRET"))
        )

        order_data = {
            "amount": int(package.price * 100),  
            "currency": "INR",
            "payment_capture": 1
        }

        order = client.order.create(data=order_data)

        # store data in session
        request.session['razorpay_order_id'] = order['id']
        request.session['package_uuid'] = str(package.uuid)

        context = {
            "RZP_CLIENT_ID": config("RZP_CLIENT_ID"),
            "order_id": order['id'],
            "amount": package.price,
            "package": package
        }

        return render(request, self.template, context)


class PaymentVerifyView(View):

    def post(self, request, *args, **kwargs):
        rzp_order_id = request.POST.get('razorpay_order_id')
        rzp_payment_id = request.POST.get('razorpay_payment_id')
        rzp_signature = request.POST.get('razorpay_signature')

        client = razorpay.Client(
            auth=(config("RZP_CLIENT_ID"), config("RZP_CLIENT_SECRET"))
        )

        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': rzp_order_id,
                'razorpay_payment_id': rzp_payment_id,
                'razorpay_signature': rzp_signature
            })

            return redirect('payment_success')

        except razorpay.errors.SignatureVerificationError:
            return redirect('payment_failed')
