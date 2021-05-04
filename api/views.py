from django.shortcuts import render
from .scripts import *


# Create your views here.
def index(request):
    # Cpu code
    cores = CPU().get_no_cores()
    total = CPU().total_cpu_usage()
    usage = CPU().usage_per_core()

    # Memory Code
    memory = Memory().memory_details()

    # Disk
    disk = Disk().get_disk_details()

    # Network
    network = Network().network_details()

    # Load Average
    loads = LoadAverage().get_load_averages()

    # Network Address
    addresses = NetworkAddress().traffic_details()

    context = {
        "cores": cores,
        "total": total,
        "usage": usage,
        "memory": memory,
        "disk": disk,
        "network": network,
        "loads": loads,
        "addresses": addresses,
    }
    return render(request, "api/index.html", context)
