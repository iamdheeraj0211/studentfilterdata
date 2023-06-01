# Generated by Django 4.2.1 on 2023-05-31 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.OneToOneField(default=22, on_delete=django.db.models.deletion.CASCADE, to='studentapp.marks'),
            preserve_default=False,
        ),
    ]