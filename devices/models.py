from django.db import models

class Device(models.Model):
    name=models.CharField(max_length=120)
    module=models.CharField(max_length=120, default='ESP32 WROOM-32E')
    rdm_model=models.CharField(max_length=80, default='RDM-503')
    status=models.CharField(max_length=40, default='disconnected')
    last_seen=models.DateTimeField(null=True, blank=True)
    def __str__(self): return self.name

class ScanLog(models.Model):
    device=models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
    timestamp=models.DateTimeField(auto_now_add=True)
    template_id=models.CharField(max_length=80, blank=True)
    result=models.CharField(max_length=40, default='unrecognized')
    note=models.CharField(max_length=200, blank=True)
    def __str__(self): return f"{self.device} • {self.result}"
