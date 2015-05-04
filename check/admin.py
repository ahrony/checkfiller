from django.contrib import admin


from check.models import *

# Register your models here.

class CheckdetailsAdmin(admin.ModelAdmin):
	list_display = ('name', 'total_ammount', 'ammount_in_word', 'date')
	

admin.site.register(Checkdetails,CheckdetailsAdmin)
