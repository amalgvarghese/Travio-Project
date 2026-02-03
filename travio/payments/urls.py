from django.urls import path

from . import views

urlpatterns=[

    path('razorpay/<uuid:uuid>/',views.RazorPayView.as_view(),name='razorpay'),

    path('payment-verify/',views.PaymentVerifyView.as_view(),name='payment_verify'),

    path('payment-success/', views.payment_success, name='payment_success'),

    path('payment-failed/', views.payment_failed, name='payment_failed'),

]
