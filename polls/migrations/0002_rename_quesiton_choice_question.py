# Generated by Django 5.0.1 on 2024-01-26 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quesiton',
            new_name='question',
        ),
    ]
