# Generated by Django 3.2.9 on 2021-11-21 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('draw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=6)),
                ('kind', models.CharField(choices=[('S', 'Квадрат'), ('C', 'Круг')], max_length=1)),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.draw')),
            ],
        ),
    ]