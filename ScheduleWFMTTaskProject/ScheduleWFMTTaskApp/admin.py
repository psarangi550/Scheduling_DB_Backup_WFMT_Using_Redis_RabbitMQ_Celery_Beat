from django.contrib import admin
from .models import WfmtTaskModel
# Register your models here.
@admin.register(WfmtTaskModel)
class WfmtTaskModelAdmin(admin.ModelAdmin):
    list_display=["id","cp_number","sne_id","scheme_number","trs","estimate"]
    
