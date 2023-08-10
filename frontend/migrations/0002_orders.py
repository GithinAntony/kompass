# Generated by Django 2.2.13 on 2020-07-06 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_title', models.CharField(max_length=100, null=True)),
                ('booking_date_text', models.CharField(max_length=100, null=True)),
                ('booking_no_of_rooms', models.CharField(max_length=100, null=True)),
                ('booking_count', models.CharField(max_length=100, null=True)),
                ('booking_price', models.CharField(max_length=100, null=True)),
                ('total_price', models.CharField(max_length=100, null=True)),
                ('date_added', models.CharField(max_length=100, null=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Place')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.User')),
            ],
        ),
    ]
