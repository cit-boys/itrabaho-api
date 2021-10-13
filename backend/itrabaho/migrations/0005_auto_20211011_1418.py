# Generated by Django 3.2.7 on 2021-10-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itrabaho', '0004_jobpostmodel_recruit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpostmodel',
            old_name='recruit',
            new_name='recruitId',
        ),
        migrations.AlterField(
            model_name='jobpostmodel',
            name='status',
            field=models.CharField(choices=[('H', 'Hiring'), ('A', 'Active'), ('D', 'Done')], default='H', max_length=1),
        ),
    ]
