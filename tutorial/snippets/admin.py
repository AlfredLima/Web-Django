from django.contrib import admin

# Register your models here.
from .models import Publication
from .models import User

admin.site.register(User)
admin.site.register(Publication)