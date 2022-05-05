from django.contrib import admin
from .models import Dopcont, Email, Famous_Persons
from .models import Authentithication
from .models import Article


# Register your models here.
class Famous_Persons_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Famous_Persons, Famous_Persons_Admin)
admin.site.register(Authentithication)
admin.site.register(Article)
admin.site.register(Email)
admin.site.register(Dopcont)

