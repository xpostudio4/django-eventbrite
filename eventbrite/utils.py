from eventbrite.models import Event, Ticket, Attendee, Contact, Venue
from eventbrite import API
from django.db.models.aggregates import Count
api = API()

def update_events(events=None):
    if not events:
        events = api.call('user_list_events',)['events']
    for event in events:
        event = event['event']
        if 'venue' in event:
            del event['venue']['Lat-Long']
            v = Venue(
                **(event['venue'])
            )

        if v.postal_code == '':
            v.postal_code = 0

        v.save()
        e = Event(
            **dict(
                (k, v) for k, v in event.items() \
                if k in set(['id', 'modified', 'privacy', 'title',
                'start_date', 'end_date', 'status', 'timezone', 'url', 'tags'])
            )
        )
        if 'venue' in event:
            e.venue = v
        e.save()
        attendee_flag = False
        if 'tickets' in event:
            for ticket in event['tickets']:
                ticket = ticket['ticket']

                if not ticket['max']:
                    ticket['max'] = 0

                t = Ticket(event=e, **ticket)
                t.save()


def update_contacts():
    events = Event.objects.annotate(count=Count('tickets')).\
    filter(
        count__gt=0, tickets__quantity_sold__gt=0
    )
    for event in events:
        attendees = api.call(
            'event_list_attendees', id=event.pk
        )['attendees']
        update_contacts_for_event(event,attendees)


def update_contacts_for_event(event,attendees):
    for attendee in attendees:
        attendee = attendee['attendee']
        attendee_ticket = Ticket.objects.get(id=attendee['ticket_id'])
        c = Contact(
            email = attendee['email'],
            first_name = attendee['first_name'],
            last_name = attendee['last_name'],
        )
        c.save()
        if not attendee['event_date']:
            del attendee['event_date']
        a = Attendee(ticket_id=attendee_ticket, contact=c,
            **dict(
                (k, v) for k, v in attendee.items() \
                if k in set([
                    'amount_paid', 'barcode', 'created', 'currency',
                    'discount', 'event_date', 'id', 'modified',
                    'order_id', 'order_type', 'quantity', 'affiliate',
                    'contact'
                ])
            )
        )
        a.save()
