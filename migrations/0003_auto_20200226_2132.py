# Generated by Django 3.0.2 on 2020-02-26 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_eheadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eheadline',
            old_name='eimage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='eheadline',
            old_name='etitle',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='eheadline',
            old_name='eurl',
            new_name='url',
        ),
    ]
