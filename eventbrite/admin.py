from django.contrib import admin
from eventbrite import models

class EventbriteEventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
admin.site.register(models.Event, EventbriteEventAdmin)


class EventbriteTicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'event',
    )
admin.site.register(models.Ticket, EventbriteTicketAdmin)


class EventbriteAttendeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'contact',
        'ticket_id',
    )
admin.site.register(models.Attendee, EventbriteAttendeeAdmin)


class EventbriteContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
    )
admin.site.register(models.Contact, EventbriteContactAdmin)


class EventbriteVenueAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
    )
admin.site.register(models.Venue, EventbriteVenueAdmin)
