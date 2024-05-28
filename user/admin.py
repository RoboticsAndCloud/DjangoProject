from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User

class UserAdmin(UserAdmin):
    add_form = UserCreationForm

    # define fields to be used in displaying the User model.

    list_display = ('first_name', 'last_name', 'email', 'organization', 'title', 'phone_number', 'start_date', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'organization','title','is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email','password1', 'password2','organization','title','phone_number','is_staff','is_active'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()
 
# Now register the new UserAdmin...

admin.site.register(User, UserAdmin)