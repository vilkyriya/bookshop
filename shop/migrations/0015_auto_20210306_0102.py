# Generated by Django 3.1.7 on 2021-03-05 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0014_auto_20210306_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id_orderbook',
            field=models.ManyToManyField(to='shop.Orderbook'),
        ),
        migrations.AddField(
            model_name='order',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='is_bought',
            field=models.BooleanField(default=False, verbose_name='Выкуплен'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False, verbose_name='Заказано'),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(null=True, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
    ]