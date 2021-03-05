# Generated by Django 3.1.7 on 2021-03-05 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'risk',
            },
        ),
        migrations.CreateModel(
            name='RiskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'risk_category',
            },
        ),
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'risk_field',
            },
        ),
        migrations.CreateModel(
            name='RiskFieldEnumOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'risk_field_enum_option',
            },
        ),
        migrations.CreateModel(
            name='RiskFieldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'risk_field_type',
            },
        ),
        migrations.CreateModel(
            name='RiskRiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_to_field', to='risk.risk')),
                ('risk_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_to_risk', to='risk.riskfield')),
            ],
            options={
                'db_table': 'risk_risk_field',
            },
        ),
        migrations.CreateModel(
            name='RiskRiskFieldRiskFieldEnumOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(default=False)),
                ('risk_field_enum_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_field_enum_option_to_risk_risk_field', to='risk.riskfieldenumoption')),
                ('risk_risk_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_risk_field_to_risk_field_enum_option', to='risk.riskriskfield')),
            ],
            options={
                'db_table': 'risk_risk_field_risk_field_enum_option',
            },
        ),
        migrations.AddField(
            model_name='riskriskfield',
            name='risk_field_enum_option',
            field=models.ManyToManyField(through='risk.RiskRiskFieldRiskFieldEnumOption', to='risk.RiskFieldEnumOption'),
        ),
        migrations.AddField(
            model_name='riskfield',
            name='risk_field_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk.riskfieldtype'),
        ),
        migrations.AddField(
            model_name='risk',
            name='risk_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk.riskcategory'),
        ),
        migrations.AddField(
            model_name='risk',
            name='risk_fields',
            field=models.ManyToManyField(through='risk.RiskRiskField', to='risk.RiskField'),
        ),
    ]
