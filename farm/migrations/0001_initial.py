# Generated by Django 4.1.10 on 2023-08-21 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=100)),
                ('starting_date', models.DateField()),
                ('harvested_crop_amount_tons', models.DecimalField(decimal_places=2, max_digits=10)),
                ('harvested_crop_price_per_ton', models.DecimalField(decimal_places=2, max_digits=10)),
                ('first_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('second_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SeasonExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.expense')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.season')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='expenses',
            field=models.ManyToManyField(through='farm.SeasonExpense', to='farm.expense'),
        ),
        migrations.AddField(
            model_name='season',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.farm'),
        ),
    ]