from django import forms

from eventbrite.models import Event

from .utils import db_table_exists

EVENT_CHOICES =(("", ""))
if db_table_exists("eventbrite_event"):
    EVENT_CHOICES = tuple([(event.id, event.title) for event in Event.objects.all()])


class EventbriteExportForm(forms.Form):
    event = forms.ChoiceField(choices=EVENT_CHOICES)
