# Generated by Django 3.1.1 on 2020-09-24 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_auto_20200924_0933'),
        ('pontosturisticos', '0003_pontosturisticos_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontosturisticos',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
        ),
    ]
