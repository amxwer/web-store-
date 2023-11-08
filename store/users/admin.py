from django.contrib import admin
from users.models import User
from products.admin import BasketAdmin
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','username','last_name','email',)
    search_fields = ('first_name','last_name','username','email')
    inlines = (BasketAdmin,)

