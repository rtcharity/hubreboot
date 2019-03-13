# Generated by Django 2.2b1 on 2019-03-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_membership'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['name', 'slug']},
        ),
        migrations.AddField(
            model_name='profile',
            name='cause_areas_other',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='expertise_areas_other',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='topics_i_speak_about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
