# Generated by Django 4.1.2 on 2022-10-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("practice", "0005_question_optione_question_optionf_and_more")]

    operations = [
        migrations.AddField(
            model_name="quastion_db",
            name="optionE",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="quastion_db",
            name="optionF",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="quastion_db",
            name="answer",
            field=models.CharField(
                choices=[
                    ("A", "A"),
                    ("B", "B"),
                    ("C", "C"),
                    ("D", "D"),
                    ("E", "E"),
                    ("F", "F"),
                ],
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="quastion_db",
            name="optionA",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="quastion_db",
            name="optionB",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="quastion_db",
            name="optionC",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="quastion_db",
            name="optionD",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
