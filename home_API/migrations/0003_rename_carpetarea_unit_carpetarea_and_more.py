# Generated by Django 4.2.3 on 2023-07-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_API', '0002_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='CarpetArea',
            new_name='carpetArea',
        ),
        migrations.AlterField(
            model_name='project',
            name='availableUnit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='brokerage',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='project',
            name='contactNumber',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='flatsPerFloors',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='floors',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='goods',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='incentive',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='landParcel',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='lifts',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='marketValue',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='power',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='readyToMove',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='totalUnit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='transport',
            field=models.BooleanField(default=False),
        ),
    ]