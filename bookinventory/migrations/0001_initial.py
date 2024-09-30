# Generated by Django 5.1.1 on 2024-09-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='title', max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('genre', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
            ],
        ),
    ]