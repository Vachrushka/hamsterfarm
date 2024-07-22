# Generated by Django 4.2.14 on 2024-07-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='new', max_length=25, verbose_name='Доступ')),
            ],
            options={
                'verbose_name': 'Доступ',
                'verbose_name_plural': 'Доступы',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Токен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('access', models.ManyToManyField(related_name='access', to='clientbase.access', verbose_name='Доступы')),
            ],
            options={
                'verbose_name': 'Токен',
                'verbose_name_plural': 'Токены',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя клиента')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
                ('tokens', models.ManyToManyField(related_name='tokens', to='clientbase.token', verbose_name='Токены')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]