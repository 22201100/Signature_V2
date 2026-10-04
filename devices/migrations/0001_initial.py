from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('module', models.CharField(default='ESP32 WROOM-32E', max_length=120)),
                ('rdm_model', models.CharField(default='RDM-503', max_length=80)),
                ('status', models.CharField(default='disconnected', max_length=40)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
            ]
        ),
        migrations.CreateModel(
            name='ScanLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('template_id', models.CharField(blank=True, max_length=80)),
                ('result', models.CharField(default='unrecognized', max_length=40)),
                ('note', models.CharField(blank=True, max_length=200)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='devices.device')),
            ]
        ),
    ]
