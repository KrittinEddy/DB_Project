# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150621_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthDate', models.DateField()),
                ('orderF', models.IntegerField(max_length=10)),
                ('orderM', models.IntegerField(max_length=10)),
                ('disable', models.CharField(max_length=1, choices=[(b'0', b''), (b'1', b'\xe0\xb9\x80\xe0\xb8\x9b\xe0\xb9\x87\xe0\xb8\x99\xe0\xb8\x9a\xe0\xb8\xb8\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\x97\xe0\xb8\xb5\xe0\xb9\x88\xe0\xb9\x84\xe0\xb8\xa3\xe0\xb9\x89\xe0\xb8\x84\xe0\xb8\xa7\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\x96\xe0\xb8\xab\xe0\xb8\xa3\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb9\x80\xe0\xb8\xaa\xe0\xb8\xa1\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x84\xe0\xb8\xa3\xe0\xb9\x89\xe0\xb8\x84\xe0\xb8\xa7\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\x96')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataFromWeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('account_id', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('user', models.OneToOneField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('pid', models.CharField(max_length=13)),
                ('user', models.OneToOneField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('family', models.OneToOneField(to='group4.Family')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_id', models.CharField(max_length=255)),
                ('disease', models.CharField(max_length=255)),
                ('hospital', models.CharField(max_length=255)),
                ('hospitalOf', models.CharField(max_length=255)),
                ('startDate', models.DateField()),
                ('stopData', models.DateField()),
                ('value', models.FloatField()),
                ('valueChar', models.CharField(max_length=255)),
                ('numBill', models.IntegerField(max_length=10)),
                ('credit', models.FloatField()),
                ('creditChar', models.CharField(max_length=255)),
                ('claim', models.CharField(max_length=1, choices=[(b'0', b''), (b'1', b'\xe0\xb8\x95\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4'), (b'2', b'\xe0\xb9\x80\xe0\xb8\x89\xe0\xb8\x9e\xe0\xb8\xb2\xe0\xb8\xb0\xe0\xb8\xaa\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\x99\xe0\xb8\x97\xe0\xb8\xb5\xe0\xb9\x88\xe0\xb8\x82\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb8\xad\xe0\xb8\xa2\xe0\xb8\xb9\xe0\xb9\x88\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\xb5\xe0\xb9\x88\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xab\xe0\xb8\x99\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x87\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\x99'), (b'3', b'\xe0\xb9\x80\xe0\xb8\x89\xe0\xb8\x9e\xe0\xb8\xb2\xe0\xb8\xb0\xe0\xb8\xaa\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\x99\xe0\xb8\x97\xe0\xb8\xb5\xe0\xb9\x88\xe0\xb8\x82\xe0\xb8\xb2\xe0\xb8\x94\xe0\xb8\xad\xe0\xb8\xa2\xe0\xb8\xb9\xe0\xb9\x88\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb1\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\x81\xe0\xb8\xb1\xe0\xb8\x99\xe0\xb8\xa0\xe0\xb8\xb1\xe0\xb8\xa2')])),
                ('selfClaim', models.CharField(max_length=1, choices=[(b'0', b''), (b'1', b'\xe0\xb9\x84\xe0\xb8\xa1\xe0\xb9\x88\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xab\xe0\xb8\x99\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x87\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\x99'), (b'2', b'\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xab\xe0\xb8\x99\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x87\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\x99\xe0\xb9\x81\xe0\xb8\x95\xe0\xb9\x88\xe0\xb9\x80\xe0\xb8\xa5\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\x81\xe0\xb9\x83\xe0\xb8\x8a\xe0\xb9\x89\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\x97\xe0\xb8\xb2\xe0\xb8\x87\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3'), (b'3', b'\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x95\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xaa\xe0\xb8\xb1\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\x81\xe0\xb8\xb1\xe0\xb8\x99\xe0\xb8\xa0\xe0\xb8\xb1\xe0\xb8\xa2'), (b'4', b'\xe0\xb9\x80\xe0\xb8\x9b\xe0\xb9\x87\xe0\xb8\x99\xe0\xb8\x9c\xe0\xb8\xb9\xe0\xb9\x89\xe0\xb9\x83\xe0\xb8\x8a\xe0\xb9\x89\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x80\xe0\xb8\x9a\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\xaa\xe0\xb8\xb3\xe0\xb8\xab\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9a\xe0\xb8\xb8\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb9\x81\xe0\xb8\x95\xe0\xb9\x88\xe0\xb9\x80\xe0\xb8\x9e\xe0\xb8\xb5\xe0\xb8\xa2\xe0\xb8\x87\xe0\xb8\x9d\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa2\xe0\xb9\x80\xe0\xb8\x94\xe0\xb8\xb5\xe0\xb8\xa2\xe0\xb8\xa7')])),
                ('familyClaim', models.CharField(max_length=1, choices=[(b'0', b''), (b'1', b'\xe0\xb9\x84\xe0\xb8\xa1\xe0\xb9\x88\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xab\xe0\xb8\x99\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x87\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\x99'), (b'2', b'\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xab\xe0\xb8\x99\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x87\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\x99\xe0\xb9\x81\xe0\xb8\x95\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x97\xe0\xb8\xb5\xe0\xb9\x88\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x95\xe0\xb9\x88\xe0\xb8\xb3\xe0\xb8\x81\xe0\xb8\xa7\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\x95\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\x9e\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\x81\xe0\xb8\xa4\xe0\xb8\xa9\xe0\xb8\x8e\xe0\xb8\xb5\xe0\xb8\x81\xe0\xb8\xb2'), (b'3', b'\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x95\xe0\xb8\xb2\xe0\xb8\xa1\xe0\xb8\xaa\xe0\xb8\xb1\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb0\xe0\xb8\x81\xe0\xb8\xb1\xe0\xb8\x99\xe0\xb8\xa0\xe0\xb8\xb1\xe0\xb8\xa2'), (b'4', b'\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb9\x84\xe0\xb8\x94\xe0\xb9\x89\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x84\xe0\xb9\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb8\x9e\xe0\xb8\xa2\xe0\xb8\xb2\xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\xa5\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\x81\xe0\xb8\xab\xe0\xb8\x99\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\x87\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\x99\xe0\xb9\x83\xe0\xb8\x99\xe0\xb8\x90\xe0\xb8\xb2\xe0\xb8\x99\xe0\xb8\xb0\xe0\xb9\x80\xe0\xb8\x9b\xe0\xb9\x87\xe0\xb8\x99\xe0\xb8\x9c\xe0\xb8\xb9\xe0\xb9\x89\xe0\xb8\xad\xe0\xb8\xb2\xe0\xb8\xa8\xe0\xb8\xb1\xe0\xb8\xa2\xe0\xb8\xaa\xe0\xb8\xb4\xe0\xb8\x97\xe0\xb8\x98\xe0\xb8\xb4\xe0\xb8\x82\xe0\xb8\xad\xe0\xb8\x87\xe0\xb8\x9c\xe0\xb8\xb9\xe0\xb9\x89\xe0\xb8\xad\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\x99')])),
                ('family', models.OneToOneField(blank=True, to='group4.Family')),
                ('user', models.OneToOneField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='child',
            name='family',
            field=models.OneToOneField(to='group4.Family'),
            preserve_default=True,
        ),
    ]
