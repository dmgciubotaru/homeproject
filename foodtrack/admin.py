from django.contrib import admin
from foodtrack.models import Category, Food


class CategoryAdmin(admin.ModelAdmin):
    pass


class FoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
