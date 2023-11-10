import csv

from django.core.management import BaseCommand
from django.conf import settings

from main.models import Category


class Command(BaseCommand):
    def  handle(self, *args, **options ):
        file_path = settings.CSC_FILE_PATH
        with open(file_path,encoding='utf-8') as file :
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                # print(row)
                Category.objects.create(name=row['name'] )