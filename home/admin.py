from django.contrib import admin
from .models import AgencyProfile, NewsArticle, Mission, TimelineEvent, SpaceObject

# Register other models
admin.site.register(NewsArticle)
admin.site.register(Mission)
admin.site.register(TimelineEvent)

class SpaceObjectInline(admin.TabularInline):
    model = SpaceObject
    extra = 1

class AgencyProfileAdmin(admin.ModelAdmin):
    list_display = ['country_name', 'agency_name', 'latitude', 'longitude', 'annual_government_spending']  # Display the new field
    inlines = [SpaceObjectInline]

if AgencyProfile in admin.site._registry:
    admin.site.unregister(AgencyProfile)
admin.site.register(AgencyProfile, AgencyProfileAdmin)
