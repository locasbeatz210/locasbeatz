# Generated by Django 2.2.1 on 2019-06-28 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mainpage.Category'),
            preserve_default=False,
        ),
    ]