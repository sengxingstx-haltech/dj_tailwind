from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)


def home(request):
    return render(request, "clients/pages/home.html")


def about(request):
    return render(request, "clients/pages/about.html")


def contact(request):
    return render(request, "clients/pages/contact.html")


def dashboard(request):
    return render(request, "dashboard/pages/dashboard.html")


def manage_profile(request):
    return render(request, "dashboard/pages/manage-profile.html")


def manage_products(request):
    context = {
        "delete_confirm_msg": "Are you sure you want to delete this product?",
    }
    return render(request, "dashboard/pages/manage-products.html", context)


def manage_users(request):
    context = {
        "delete_confirm_msg": "Are you sure you want to delete this user?",
    }
    return render(request, "dashboard/pages/manage-users.html", context)
