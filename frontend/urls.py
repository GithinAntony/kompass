from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('search-category/<int:id>', views.search_category, name='search-category'),
    path('search-places/<int:id>/<str:str_type>', views.search_places, name='search-places'),

    path('place-details/<int:id>', views.place_details, name='place-details'),
    path('places/delete/<int:id>', views.places_delete),

    path('admin-login', views.site_admin_login, name='site-admin-login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('owner-login', views.owner_login, name='owner-login'),
    path('owner-register', views.owner_register, name='owner-register'),

    path('logout', views.logout, name='logout'),

    path('user-dashboard', views.user_dashboard, name='user-dashboard'),
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    path('admin-users', views.admin_users, name='admin-users'),
    path('admin-users/delete/<int:user_id>', views.admin_users_delete,
         name='admin-users-delete'),
    path('admin-users/status/<int:user_id>/<slug:slug>', views.admin_users_status,
         name='admin-users-status'),

    path('admin-contact-us', views.admin_contact_us, name='admin_contact_us'),
    path('admin-locality', views.admin_locality, name='admin-locality'),
    path('admin-locality/delete/<int:id>', views.admin_locality_delete, name='admin-locality-delete'),

    path('admin-amenity', views.admin_amenity, name='admin-amenity'),
    path('admin-amenity/delete/<int:id>', views.admin_amenity_delete, name='admin-amenity-delete'),

    path('admin-places', views.admin_places, name='admin-places'),
    path('admin-places/delete/<int:id>', views.admin_places_delete,
         name='admin-users-delete'),
    path('admin-places/status/<int:id>/<slug:slug>', views.admin_places_status,
         name='admin-users-status'),

    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('addnewplace', views.addnewplace, name='addnewplace'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('myplaces', views.myplaces, name='myplaces'),
    path('pendingplaces', views.pendingplaces, name='pendingplaces'),
    path('user-gallery/<int:place_id>', views.user_gallery, name='user-gallery'),
    path('user-gallery/delete/<int:place_id>/<int:id>', views.user_gallery_delete, name='user-gallery-delete'),
    path('user-place-report/<int:place_id>',views.user_place_report, name='user-place-report'),
    path('user-place-booking-day/<int:place_id>', views.user_place_booking_day, name='user-place-day'),
    path('user-place-booking-seat/<int:place_id>', views.user_place_booking_seat, name='user-place-seat'),
    path('user-place-booking-ticket/<int:place_id>', views.user_place_booking_ticket, name='user-place-ticket'),
    path('user-booking-payment/<int:place_id>',views.user_booking_payment, name='user-booking-payment'),
    path('user-booking-payment-success/<int:place_id>', views.user_booking_payment_success, name='user-booking-payment-success'),
    path('user-booking-orders',views.user_booking_orders, name='user-booking-orders'),
    path('place-booking-orders/<int:place_id>', views.place_booking_orders, name='place-booking-orders'),
    path('forgot-password/<str:usertype>', views.forgot_password, name='forgot-password'),
    path('user-change-password', views.user_change_password, name='user-change-password'),
    path('owner-change-password', views.owner_change_password, name='owner-change-password'),
    path('user-edit-profile', views.user_edit_profile, name='user-edit-profile'),
    path('owner-edit-profile', views.owner_edit_profile, name='owner-edit-profile'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)