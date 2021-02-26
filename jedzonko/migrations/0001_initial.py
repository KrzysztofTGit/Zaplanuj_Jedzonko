# Generated by Django 2.2.6 on 2021-02-24 15:50


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dayname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'Poniedziałek'), (2, 'Wtorek'), (3, 'Środa'), (4, 'Czwartek'), (5, 'Piątek'), (6, 'Sobota'), (7, 'Niedziela')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('ingredients', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=1200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('preparation_time', models.SmallIntegerField(default=0)),
                ('preparation_method', models.TextField(max_length=1200)),
                ('votes', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RecipePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_names', models.IntegerField(choices=[(1, 'Śniadanie'), (2, 'Drugie śniadanie'), (3, 'Obiad'), (4, 'Podwieczorek'), (5, 'Kolacja')], default=1)),
                ('order', models.IntegerField()),
                ('day_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Dayname')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Plan')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='recipes',
            field=models.ManyToManyField(through='jedzonko.RecipePlan', to='jedzonko.Recipe'),
        ),
    ]
