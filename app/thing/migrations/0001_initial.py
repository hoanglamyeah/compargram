# Generated by Django 2.0.3 on 2018-03-28 10:12

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0002_auto_20180327_1626'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=60)),
                ('allow_foreign_compare', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('created_date', models.DateField(auto_now=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classify_image', to='media.Image')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_classify', to='thing.Classify')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=120)),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=60)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_classify', to='thing.Classify')),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('classify', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thing_classify', to='thing.Classify')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thing_creator', to=settings.AUTH_USER_MODEL)),
                ('photos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now=True)),
                ('thing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_thing', to='thing.Thing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compare',
            name='first',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_compare', to='thing.Thing'),
        ),
        migrations.AddField(
            model_name='compare',
            name='second',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_compare', to='thing.Thing'),
        ),
        migrations.AddField(
            model_name='comment',
            name='compare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_thing', to='thing.Compare'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
