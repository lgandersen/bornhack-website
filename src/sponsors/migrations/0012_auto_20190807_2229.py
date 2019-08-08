# Generated by Django 2.2.3 on 2019-08-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0011_auto_20181118_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='ticket_email',
            field=models.EmailField(blank=True, help_text='The email to send the tickets to', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='ticket_ready',
            field=models.BooleanField(default=False, help_text='Check when we are ready to send tickets to this sponsor.'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='tickets_sent',
            field=models.BooleanField(default=False, help_text='True when the tickets have been emailed to the sponsor'),
        ),
    ]
