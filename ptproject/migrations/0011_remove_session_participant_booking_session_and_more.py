# Generated by Django 4.2.7 on 2024-02-12 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ptproject.models
import ptproject.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ptproject', '0010_auto_20240212_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='participant',
        ),
        migrations.AddField(
            model_name='booking',
            name='session',
            field=models.ForeignKey(default=ptproject.models.get_default_session, null=True, on_delete=django.db.models.deletion.CASCADE, to='ptproject.session'),
        ),
        migrations.AddField(
            model_name='session',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[ptproject.utils.num_validation]),
        ),
    ]
