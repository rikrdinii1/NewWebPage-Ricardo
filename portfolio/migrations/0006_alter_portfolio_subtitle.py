# Generated by Django 4.1.7 on 2023-03-22 05:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0005_alter_portfolio_subtitle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="subtitle",
            field=ckeditor.fields.RichTextField(blank=True, max_length=300),
        ),
    ]