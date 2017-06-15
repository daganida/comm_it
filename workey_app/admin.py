from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from workey_app.models import Worker, Task

admin.site.register(Worker)
admin.site.register(Task)

admin.site.unregister(User)

class MyUserAdmin(admin.ModelAdmin):
    exclude = ('last_login', 'groups', 'user_permissions', 'is_active','date_joined', 'is_staff', 'is_superuser', 'password')

admin.site.register(User,MyUserAdmin)
