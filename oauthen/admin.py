from django.contrib import admin
from .models  import User ,issue,Food , MealLog 

class FoodAdmin(admin.ModelAdmin):
    search_fields = ['food_name']

admin.site.register(User) 
admin.site.register(issue) 
admin.site.register(Food, FoodAdmin) 
admin.site.register(MealLog)