# Generated by Django 2.1.7 on 2019-03-27 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0002_auto_20190318_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionUserNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_private', models.BooleanField(default=True)),
                ('note', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='subscriptionusermessage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='subscriptionusermessage',
            name='subscription',
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['end_date'], 'permissions': (('can_view_all_subscriptions', 'Can view all subscriptions'), ('can_review_subscription_requests', 'Can review subscription requests'), ('can_manage_invoice', 'Can manage invoice'))},
        ),
        migrations.DeleteModel(
            name='SubscriptionUserMessage',
        ),
        migrations.AddField(
            model_name='subscriptionusernote',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.Subscription'),
        ),
    ]
