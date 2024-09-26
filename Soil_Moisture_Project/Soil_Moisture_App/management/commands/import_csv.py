import csv
from django.core.management.base import BaseCommand
from Soil_Moisture_App.models import SoilData

class Command(BaseCommand):
    help = 'Import soil data from CSV'

    def handle(self, *args, **kwargs):
        file_path = 'soil_moisture.csv'
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                SoilData.objects.create(
                    date=row['date'],
                    time=row['time'],
                    location=row['location'],
                    temperature=float(row['temperature']),
                    humidity=float(row['humidity']),
                    soil_texture=row['soil_texture'],
                    rainfall=float(row['rainfall']),
                    soil_moisture=float(row['soil_moisture'])
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
