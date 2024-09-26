
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Soil_Moisture_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soildata',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
