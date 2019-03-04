# Generated by Django 2.1.7 on 2019-03-03 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=100)),
                ('accountNoReceiver', models.CharField(max_length=8)),
                ('sortCodeReceiver', models.CharField(max_length=6)),
                ('value', models.IntegerField()),
                ('transactionDetails', models.CharField(max_length=100)),
                ('date_transaction', models.DateTimeField(default=django.utils.timezone.now)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]