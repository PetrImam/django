import csv
from django.core.management.base import BaseCommand
from phones.models import Phone  # Замените 'phones' на имя вашего приложения, если оно другое

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:  # Укажите путь к вашему CSV-файлу
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                Phone.objects.create(
                    id=int(row['id']),
                    name=row['name'],
                    image=row['image'],
                    price=float(row['price']),
                    release_date=row['release_date'],
                    lte_exists=bool(row['lte_exists'] == 'True')
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))