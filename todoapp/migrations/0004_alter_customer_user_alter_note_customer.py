# Generated by Django 4.1.2 on 2022-12-23 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_remove_note_user_customer_note_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapp.customer'),
        ),
    ]
