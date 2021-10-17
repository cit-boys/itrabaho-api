# Generated by Django 3.2.7 on 2021-10-17 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itrabaho', '0009_auto_20211016_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantmodel',
            name='profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='itrabaho.profilemodel'),
        ),
        migrations.AlterField(
            model_name='experiencedetailmodel',
            name='experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='itrabaho.experiencemodel'),
        ),
        migrations.AlterField(
            model_name='experiencemodel',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiencemodel',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='itrabaho.profilemodel'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='highesteducationAttained',
            field=models.CharField(choices=[('N', 'None'), ('E', 'Elementary'), ('H', 'High School'), ('U', 'College Undergraduate'), ('B', "Bachelor's Degree"), ('A', 'Associate Degree'), ('M', "Master's Degree"), ('D', 'Doctorate Degree')], max_length=1),
        ),
    ]