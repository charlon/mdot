# Generated by Django 2.0.13 on 2021-09-02 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdot', '0004_remove_manager_to_app'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreement',
            old_name='app',
            new_name='corresp_app',
        ),
        migrations.AddField(
            model_name='app',
            name='app_agreement',
            field=models.ForeignKey(
                default=False,
                on_delete=django.db.models.deletion.CASCADE,
                to='mdot.Agreement'
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agreement',
            name='agree',
            field=models.BooleanField(),
        ),
    ]
