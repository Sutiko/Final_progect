# Generated by Django 4.1.2 on 2022-10-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('gel', 'gel'), ('gel-lack', 'gel-lack'), ('base', 'base'), ('top', 'top')], max_length=100, null=True),
        ),
    ]