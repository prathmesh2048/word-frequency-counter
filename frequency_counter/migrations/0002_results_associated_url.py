# Generated by Django 3.1.6 on 2021-02-06 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frequency_counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='associated_url',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='frequency_counter.web_address'),
        ),
    ]
