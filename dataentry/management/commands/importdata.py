from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
import csv

# Proposed command - python manage.py importdata file_path model_name

class Command(BaseCommand):
    help = "Import data from CSV File"
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV File')
        parser.add_argument('model_name', type=str, help='Name of the model')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        #Search for models across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # Try to search for the model in the app
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported fully!'))