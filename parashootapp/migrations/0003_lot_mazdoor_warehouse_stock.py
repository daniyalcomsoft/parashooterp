# Generated by Django 4.1.2 on 2023-12-05 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parashootapp', '0002_categoryfour_categoryone_categorythree_categorytwo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('LotID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Lot Name')),
            ],
        ),
        migrations.CreateModel(
            name='Mazdoor',
            fields=[
                ('MazdoorID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Mazdoor Name')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('WarehouseID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Warehouse Name')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('StockID', models.AutoField(primary_key=True, serialize=False)),
                ('LabourAmount', models.BigIntegerField(verbose_name='Labour Amount')),
                ('Quantity', models.BigIntegerField(verbose_name='Quantity')),
                ('Lot', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parashootapp.lot', verbose_name='Lot Name')),
                ('Mazdoor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parashootapp.mazdoor', verbose_name='Mazdoor Name')),
                ('Options', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parashootapp.options', verbose_name='Option Name')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parashootapp.product', verbose_name='Product Name')),
                ('Warehouse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parashootapp.warehouse', verbose_name='Warehouse Name')),
            ],
        ),
    ]