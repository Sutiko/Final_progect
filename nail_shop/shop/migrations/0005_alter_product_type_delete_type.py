# Generated by Django 4.1.2 on 2022-10-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('base', 'base'), ('gel', 'gel'), ('top', 'top'), ('gel-lack', 'gel-lack')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]