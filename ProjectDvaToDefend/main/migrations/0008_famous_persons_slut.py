# Generated by Django 4.0.2 on 2022-04-07 14:26

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_famous_persons_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='famous_persons',
            name='slut',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name']),
        ),
    ]
