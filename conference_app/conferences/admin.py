from django.contrib import admin

from conferences.models import Conference

from events.models import Event

# Klasė nurodanti, kokie dar susiję modeliai turėtų būti vaizduojami konferencijos lange
# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#inlinemodeladmin-options
class EventInline(admin.TabularInline):
    model = Event
    extra = 1
# Dokumentacija: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#modeladmin-options
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date' ]
    inlines = [EventInline]

admin.site.register(Conference,ConferenceAdmin)