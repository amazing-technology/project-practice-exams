# Generated by Django 4.1.2 on 2022-10-23 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("practice", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="users", old_name="fullname", new_name="fullName"
        ),
        migrations.RemoveField(model_name="users", name="timestamps"),
    ]
