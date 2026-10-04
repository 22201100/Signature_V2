from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Device, ScanLog
from .forms import DeviceForm

@login_required
def device_list(request):
    items = Device.objects.all().order_by('name')
    return render(request, 'devices/list.html', {'items': items})

@login_required
def device_create(request):
    if request.method=='POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device added.')
            return redirect('device_list')
        messages.error(request, 'Fix errors below.')
    else:
        form = DeviceForm()
    return render(request, 'devices/form.html', {'form': form, 'title':'Add Device'})

@login_required
def device_update(request, pk):
    obj = get_object_or_404(Device, pk=pk)
    if request.method=='POST':
        form = DeviceForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device updated.')
            return redirect('device_list')
        messages.error(request, 'Fix errors below.')
    else:
        form = DeviceForm(instance=obj)
    return render(request, 'devices/form.html', {'form': form, 'title':'Update Device'})

@login_required
def device_delete(request, pk):
    obj = get_object_or_404(Device, pk=pk)
    if request.method=='POST':
        obj.delete()
        messages.success(request, 'Device deleted.')
        return redirect('device_list')
    return render(request, 'devices/confirm_delete.html', {'obj': obj})

@login_required
def connect(request):
    if request.method=='POST':
        name = request.POST.get('name','ESP32-WROOM-32E #1')
        dev, _ = Device.objects.get_or_create(name=name)
        dev.status='connected'
        dev.last_seen=timezone.now()
        dev.save()
        ScanLog.objects.create(device=dev, template_id='T-0001', result='matched', note='demo connect')
        messages.success(request, f'{dev.name} connected.')
        return redirect('device_list')
    return render(request, 'devices/connect.html')

@login_required
def device_logs(request, pk):
    dev = get_object_or_404(Device, pk=pk)
    logs = dev.logs.order_by('-timestamp')[:300]
    return render(request, 'devices/logs.html', {'device': dev, 'logs': logs})
