# Generated by Django 4.1.10 on 2023-08-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_km', models.PositiveIntegerField()),
                ('ending_km', models.PositiveIntegerField()),
                ('money_collected', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_online_payment', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(blank=True, max_length=50, null=True)),
                ('expenses', models.DecimalField(decimal_places=2, max_digits=10)),
                ('diesel', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.RenameModel(
            old_name='OverallTransportExpenses',
            new_name='Expenses',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
    ]
