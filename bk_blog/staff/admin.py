from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import StaffMember


class StaffMemberAdmin(ModelAdmin):
    model = StaffMember
    list_display = "name"
    menu_icon = "user"
    menu_order = 300


modeladmin_register(StaffMemberAdmin)
