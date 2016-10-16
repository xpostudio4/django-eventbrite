import csv

from eventbrite import models
from eventbrite.utils import update_contacts, update_events

from django.conf.urls import patterns
from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from .forms import EventbriteExportForm


class EventAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super(EventAdmin, self).get_urls()

        my_urls = patterns('',
            (r'^report/$', self.admin_site.admin_view(self.GenerateReport.as_view())),
            (r'^sync/$', self.admin_site.admin_view(self.SyncEventbriteView.as_view())),
        )

        return my_urls + urls

    class SyncEventbriteView(RedirectView):
        url = '/admin/eventbrite/'

        def get_redirect_url(self, *args, **kwargs):
            update_events()
            update_contacts()
            messages.add_message(self.request, messages.INFO, "Eventbrite info was updated")
            return self.url

    class GenerateReport(FormView):
        form_class = EventbriteExportForm
        template_name = 'admin/eventbrite/report.html'
        success_url = '/admin/eventbrite/events/'

        def form_valid(self, form):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="example.csv"'

            event_id = form['event'].value()

            tickets = models.Event.objects.get(id=event_id).tickets.all()
            writer = csv.writer(response)
            writer.writerow(["Event", "First_name", "Last_name", "Email", "Ticket no.", "Order No.", "Event Date"])
            for ticket in tickets:
                attendees = models.Attendee.objects.filter(ticket_id=ticket.id)
                for attendee in attendees:
                    values = [
                            ticket.event.title,
                            attendee.contact.first_name,
                            attendee.contact.last_name,
                            attendee.contact.email,
                            attendee.ticket_id,
                            attendee.order_id,
                            ticket.event.start_date,
                    ]
                    writer.writerow(values)

            return response

admin.site.register(models.Event, EventAdmin)


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
