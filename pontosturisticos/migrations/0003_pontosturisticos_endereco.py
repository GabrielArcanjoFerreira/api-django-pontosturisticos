# Generated by Django 3.1.1 on 2020-09-24 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_auto_20200924_0933'),
        ('pontosturisticos', '0002_auto_20200924_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
            preserve_default=False,
        ),
    ]