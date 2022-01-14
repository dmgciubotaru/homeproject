from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from foodtrack.models import Food


@login_required
def main_page(request):
    foods = Food.objects.all()
    return render(request, "foodtrack/foodlist.html", {"foods": foods})

