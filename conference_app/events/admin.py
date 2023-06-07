from django.contrib import admin

from events.models import Event  # Tas pats kaip from events.models import Event
# Taip galim daryti nes esame tam paciam aplanke

# Register your models here.
admin.site.register (Event)