# Generated by Django 4.2.6 on 2023-10-28 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_rename_receipre_receipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='receipe_descriprion',
            new_name='receipe_description',
        ),
    ]
