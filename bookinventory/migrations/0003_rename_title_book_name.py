# Generated by Django 5.1.1 on 2024-09-29 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookinventory', '0002_remove_book_name_book_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='name',
        ),
    ]
