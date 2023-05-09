# Generated by Django 4.2.1 on 2023-05-09 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('plane_model', models.CharField(max_length=100)),
                ('number_of_rows', models.IntegerField()),
                ('seats_per_row', models.IntegerField()),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('origin', models.CharField(max_length=5)),
                ('destination', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('passenger_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('passport_number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat_number', models.IntegerField()),
                ('seat_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('hold_luggage', models.BooleanField()),
                ('payment_confirmed', models.BooleanField()),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.passenger')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.seat')),
            ],
        ),
    ]