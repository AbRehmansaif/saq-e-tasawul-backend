# Generated by Django 5.1.3 on 2025-01-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category Name')),
                ('description', models.TextField(verbose_name='Category Description')),
                ('image', models.ImageField(null=True, upload_to='category_image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
