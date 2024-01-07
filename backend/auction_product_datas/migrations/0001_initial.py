# Generated by Django 4.2.5 on 2023-11-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auction_fooditems',
            },
        ),
        migrations.CreateModel(
            name='FoodInventory',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_bidding_placed', models.PositiveIntegerField(default=0)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('current_time', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(related_name='auction_fooditems', to='auction_product_datas.fooditem')),
            ],
            options={
                'db_table': 'auction_fooditems_inventory',
            },
        ),
    ]
