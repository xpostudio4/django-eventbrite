from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from eventbrite.utils import update_contacts

class Command(BaseCommand):
    help = 'Help text goes here'

    def handle(self, **options):
        return update_contacts()
