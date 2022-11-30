from home.forms import GroupAdminForm
from django.contrib import admin
from .models import Visitors
from django.contrib.auth.models import Group

admin.site.register(Visitors)
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)