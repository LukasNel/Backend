# Generated by Django 3.2 on 2022-04-09 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yutorapp', '0005_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttimeslot',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_times', to='yutorapp.request'),
        ),
    ]
