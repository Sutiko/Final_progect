# Generated by Django 4.1.2 on 2022-10-17 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_type_delete_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('gel-lack', 'gel-lack'), ('top', 'top'), ('base', 'base'), ('gel', 'gel')], max_length=100, null=True),
        ),
    ]
