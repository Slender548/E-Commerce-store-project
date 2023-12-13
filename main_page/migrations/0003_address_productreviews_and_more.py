# Generated by Django 4.2.7 on 2023-12-09 17:11

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_basket_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('house', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('photos', models.ImageField(upload_to='ProductReviews')),
                ('likes', models.IntegerField(default=0)),
                ('review', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='placed',
            new_name='added_on',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcategories',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Subcategories', to='main_page.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='apartment',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='house',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='^\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Users'),
        ),
        migrations.AddField(
            model_name='user',
            name='registered_on',
            field=models.DateField(auto_now_add=True, default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(to='main_page.product'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Basket', to='main_page.user'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='main_page.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('addresses', models.ManyToManyField(related_name='SellerAddresses', to='main_page.address')),
                ('reviews', models.ManyToManyField(related_name='Seller', to='main_page.productreviews')),
            ],
        ),
        migrations.AddField(
            model_name='productreviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductReviews', to='main_page.product'),
        ),
        migrations.AddField(
            model_name='productreviews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductReviews', to='main_page.user'),
        ),
        migrations.CreateModel(
            name='ProductReviewComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='main_page.productreviews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.user')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='main_page.seller'),
        ),
    ]