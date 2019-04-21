# Generated by Django 2.2 on 2019-04-20 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockcaregh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Advil', max_length=20)),
                ('serial', models.IntegerField(default='12332109878')),
            ],
        ),
        migrations.AlterModelOptions(
            name='pharmacy',
            options={'verbose_name': 'Pharmacie'},
        ),
        migrations.AddField(
            model_name='distributor',
            name='product',
            field=models.ManyToManyField(to='blockcaregh.Product'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='product',
            field=models.ForeignKey(default=123456789, on_delete=django.db.models.deletion.CASCADE, to='blockcaregh.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='product',
            field=models.ManyToManyField(to='blockcaregh.Product'),
        ),
    ]