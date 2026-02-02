from django.urls import path

from . import views

urlpatterns=[

    path('',views.HomeView.as_view(),name='home'),
    
    path('package-list/',views.PackageListView.as_view(),name='package-list'),

    path('package-create/',views.PackageCreateView.as_view(),name='package-create'),

    path('package-details/<uuid:uuid>/',views.PackageDetailsView.as_view(),name='package-details'),

    path('services/',views.ServiceView.as_view(),name='services'),

    path('package-edit/<str:uuid>/',views.PackageEditView.as_view(),name='package-edit'),

    path('package-delete/<str:uuid>/',views.PackageDeleteView.as_view(),name='package-delete'),

    path('about/',views.AboutView.as_view(),name='about'),

    path('contact/',views.contactView.as_view(),name='contact'),

    ]