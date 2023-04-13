from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "KIPAGA "
admin.site.site_title = "Gerenciador"
admin.site.index_title = "KIPAGA"


admin.site.register(Deposito)
admin.site.register(empresa)
admin.site.register(Transferencia)
admin.site.register(notify)

