# Generated by Django 4.1.10 on 2023-08-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenses_type', models.CharField(choices=[('food', 'Food'), ('medicine', 'Medicine'), ('grass', 'Grass'), ('other', 'Other')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Grass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_mobile', models.CharField(max_length=15)),
                ('total_amount_grass', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_to_be_paid', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('labor_type', models.CharField(choices=[('monthly', 'Monthly'), ('daily', 'Daily')], max_length=20)),
                ('payment_to_be_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
