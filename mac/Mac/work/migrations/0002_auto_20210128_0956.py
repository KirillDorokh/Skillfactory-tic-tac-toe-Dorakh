# Generated by Django 3.1.5 on 2021-01-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productorder',
            old_name='amount',
            new_name='_amount',
        ),
        migrations.AlterField(
            model_name='productorder',
            name='_amount',
            field=models.IntegerField(db_column='amount', default=1),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(max_length=255),
        ),
    ]
