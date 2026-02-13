import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Импорт телефонов из CSV-файла'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:  # phones.csv в корне проекта
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': row['name'],
                        'image': row['image'],
                        'price': float(row['price']),
                        'release_date': row['release_date'],
                        'lte_exists': row['lte_exists'].lower() == 'true',
                        'slug': row['name'].lower().replace(' ', '-'),  # Простой slug, если slugify не используется
                    }
                )
        self.stdout.write(self.style.SUCCESS('Телефоны успешно импортированы'))