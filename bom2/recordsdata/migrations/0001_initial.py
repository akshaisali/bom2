# Generated by Django 4.0.6 on 2024-08-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConveyorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('80', '80'), ('100', '100'), ('120', '120')], max_length=10)),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=10)),
                ('specification', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bom', models.CharField(choices=[('washing_80', 'Washing Equipment 80'), ('washing_100', 'Washing Equipment 100'), ('washing_120', 'Washing Equipment 120'), ('furnace_80', 'Furnace Equipment 80'), ('furnace_100', 'Furnace Equipment 100'), ('furnace_120', 'Furnace Equipment 120'), ('tempering_80', 'Tempering Equipment 80'), ('tempering_100', 'Tempering Equipment 100'), ('tempering_120', 'Tempering Equipment 120'), ('conveyor_80', 'Conveyor Equipment 80'), ('conveyor_100', 'Conveyor Equipment 100'), ('conveyor_120', 'Conveyor Equipment 120')], max_length=20, verbose_name='Equipment BOM')),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=20, verbose_name='Model')),
                ('components', models.JSONField(verbose_name='Components')),
                ('specification', models.TextField(verbose_name='Specification')),
                ('make', models.CharField(max_length=100, verbose_name='Make')),
                ('purpose', models.CharField(max_length=100, verbose_name='Purpose')),
                ('quality', models.CharField(max_length=100, verbose_name='Quality')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='FrontdoorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('80', '80'), ('100', '100'), ('120', '120')], max_length=10)),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=10)),
                ('specification', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='FurnaceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('80', '80'), ('100', '100'), ('120', '120')], max_length=10)),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=10)),
                ('specification', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PreheatingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('80', '80'), ('100', '100'), ('120', '120')], max_length=10)),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=10)),
                ('specification', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TemperingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bom', models.CharField(choices=[('tempering_80', 'Tempering Equipment 80'), ('tempering_100', 'Tempering Equipment 100'), ('tempering_120', 'Tempering Equipment 120')], max_length=100)),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=100)),
                ('specification', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WashingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('80', '80'), ('100', '100'), ('120', '120')], max_length=10)),
                ('model', models.CharField(choices=[('model_a', 'Model A'), ('model_b', 'Model B'), ('model_c', 'Model C')], max_length=10)),
                ('specification', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
