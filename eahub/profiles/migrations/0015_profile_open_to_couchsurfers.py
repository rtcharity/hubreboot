# Generated by Django 2.2.10 on 2020-04-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0014_profile_is_approved")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="open_to_couchsurfers",
            field=models.BooleanField(blank=True, default=None, null=True),
        )
    ]
