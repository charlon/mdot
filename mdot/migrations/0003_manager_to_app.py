# Generated by Django 2.0.13 on 2021-09-02 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdot', '0002_auto_20210826_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='to_app',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='mdot.App',
                editable=False
            ),
        ),
    ]
