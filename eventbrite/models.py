from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    modified = models.DateTimeField(blank=False)
    privacy = models.CharField(max_length=15, blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    status = models.CharField(max_length=15, blank=False)
    timezone = models.CharField(max_length=15, blank=False)
    title = models.CharField(max_length=60, blank=False)
    url = models.URLField(blank=False)
    tags = models.CharField(max_length=30, blank=True)
    venue = models.ForeignKey('Venue', null=True)
    def __unicode__(self):
        return self.title
    
class Ticket(models.Model):
    currency = models.CharField(max_length=4, blank=False)
    description = models.TextField()
    end_date = models.DateTimeField(blank=False)
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=5, blank=False)
    quantity_available = models.PositiveIntegerField(blank=False)
    quantity_sold  = models.PositiveIntegerField(blank=False)
    type = models.SmallIntegerField(blank=False)
    visible = models.BooleanField(blank=False)
    event = models.ForeignKey('Event', related_name='tickets')
    
    def __unicode__(self):
        return '%s: %s' % (self.event.title, self.name)

    
class Attendee(models.Model):
    amount_paid = models.DecimalField(decimal_places=2, max_digits=5, blank=False)
    barcode = models.CommaSeparatedIntegerField(max_length=200,blank=False)
    created = models.DateTimeField(blank=False)
    currency = models.CharField(max_length=4, blank=False)
    discount = models.CharField(max_length=20,)
    event_date = models.DateTimeField(blank=True, null=True)
    id = models.PositiveIntegerField(primary_key=True)
    modified = models.DateTimeField(blank=False)
    order_id = models.PositiveIntegerField(blank=False)
    order_type = models.CharField(max_length=15, blank=False)
    quantity = models.PositiveIntegerField(blank=False)
    ticket_id = models.ForeignKey('Ticket', related_name='attendees')
    affiliate = models.CharField(max_length=30,)
    contact = models.ForeignKey('Contact', related_name='attendees')


class Contact(models.Model):
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    email = models.EmailField(primary_key=True)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
        
        
class Venue(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    address_2 = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    region = models.CharField(max_length=20)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=5)
    longitude = models.FloatField(blank=False)
    latitude =  models.FloatField(blank=False)
    
