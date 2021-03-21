# Generated by Django 2.2.17 on 2021-03-21 13:28

import django.core.validators
from django.db import migrations, models

import eahub.profiles.validators
from eahub.profiles.models import Profile


def transform_field_name_to_first_name(apps, schema_editor):
    for profile in Profile.objects.all():
        *first_name_list, last_name = profile.first_name.split()
        if first_name_list:
            profile.first_name = " ".join(first_name_list)
            profile.last_name = last_name
        else:
            profile.first_name = last_name
        profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0021_alter_bool_fields_by_preventing_null"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="name",
            new_name="first_name",
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.CharField(
                default="",
                max_length=200,
                validators=[eahub.profiles.validators.validate_sluggable_name],
            ),
            preserve_default=False,
        ),
        migrations.RunPython(
            code=transform_field_name_to_first_name,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="profile",
            name="allow_messaging",
            field=models.BooleanField(
                default=True, verbose_name="Allow approved users to message me"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="available_as_speaker",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="profile",
            name="available_to_volunteer",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="profile",
            name="facebook_url",
            field=models.URLField(blank=True, max_length=400, verbose_name="Facebook"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="is_public",
            field=models.BooleanField(
                default=True,
                help_text="Unchecking this will completely conceal your profile",
                verbose_name="Public profile",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="linkedin_url",
            field=models.URLField(blank=True, max_length=400, verbose_name="Linkedin"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="open_to_job_offers",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="profile",
            name="personal_website_url",
            field=models.URLField(
                blank=True, max_length=400, verbose_name="Personal website"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="summary",
            field=models.TextField(
                blank=True,
                validators=[django.core.validators.MaxLengthValidator(6000)],
                verbose_name="Bio",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="topics_i_speak_about",
            field=models.TextField(
                blank=True,
                validators=[django.core.validators.MaxLengthValidator(2000)],
                verbose_name="Topics I speak about other",
            ),
        ),
    ]
