# Generated by Django 4.0.3 on 2023-11-28 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
        ('rounge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule', verbose_name='schedule'),
        ),
    ]