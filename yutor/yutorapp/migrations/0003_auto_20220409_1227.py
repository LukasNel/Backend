# Generated by Django 3.2 on 2022-04-09 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yutorapp', '0002_remove_tutor_pub_date_tutor_bio_tutor_numratings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='time_request',
        ),
        migrations.AlterField(
            model_name='request',
            name='Tutee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yutorapp.tutee'),
        ),
        migrations.AlterField(
            model_name='request',
            name='Tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yutorapp.tutor'),
        ),
        migrations.AlterField(
            model_name='transactiontable',
            name='Tutee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yutorapp.tutee'),
        ),
        migrations.AlterField(
            model_name='transactiontable',
            name='Tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yutorapp.tutor'),
        ),
        migrations.AlterField(
            model_name='tutee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RequestTimeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='start time')),
                ('end', models.DateTimeField(verbose_name='end time')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_times', to='yutorapp.request')),
            ],
        ),
    ]
