# Generated by Django 2.2.10 on 2020-04-13 12:01

import django.contrib.postgres.fields
from django.db import migrations
import django_enumfield.db.fields
import eahub.localgroups.models

def copy_group_type(apps, schema_editor):
    LocalGroup = apps.get_model("localgroups", "LocalGroup")
    for row in LocalGroup.objects.all():
        if row.local_group_type:
            row.local_group_types=[row.local_group_type]
            row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('localgroups', '0004_localgroup_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='localgroup',
            name='local_group_types',
            field=django.contrib.postgres.fields.ArrayField(base_field=django_enumfield.db.fields.EnumField(default=1, enum=eahub.localgroups.models.LocalGroupType), blank=True, default=list, size=None),
        ),
        migrations.RunPython(copy_group_type)
    ]
