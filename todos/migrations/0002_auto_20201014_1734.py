# Generated by Django 3.1.2 on 2020-10-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Item',
        ),
    ]