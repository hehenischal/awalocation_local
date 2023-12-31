# Generated by Django 4.2.2 on 2023-06-30 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('things_to_do', models.CharField(max_length=200)),
                ('best_time_to_visit', models.CharField(max_length=200)),
                ('unique_features', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Accomodation', 'Accomodation'), ('Cultural', 'Cultural'), ('Historic', 'Historic'), ('Others', 'Others')], default='Others', max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('author_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.description')),
            ],
        ),
    ]
