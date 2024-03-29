# Generated by Django 2.2.4 on 2019-09-16 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='friends',
        ),
        migrations.AddField(
            model_name='contact',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='_contact_contacts_+', to='chat.Contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
