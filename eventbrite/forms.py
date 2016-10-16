from django import forms

from eventbrite.models import Event

EVENT_CHOICES = tuple([(event.id, event.title) for event in Event.objects.all()])


class EventbriteExportForm(forms.Form):
    event = forms.ChoiceField(choices=EVENT_CHOICES)
