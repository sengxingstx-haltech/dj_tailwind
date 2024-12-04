from django.conf.urls import handler404
from django.urls import include, path

from . import views as core_views

handler404 = core_views.custom_404_view

urlpatterns = [
    path("", core_views.home, name="home"),
    path("about/", core_views.about, name="about"),
    path("contact/", core_views.contact, name="contact"),
    path("dashboard/", core_views.dashboard, name="dashboard"),
    path("dashboard/profile", core_views.manage_profile, name="manage-profile"),
    path("dashboard/manage-products/", core_views.manage_products, name="manage-products"),
    path("dashboard/manage-users/", core_views.manage_users, name="manage-users"),
    path("accounts/", include("accounts.urls")),
]
