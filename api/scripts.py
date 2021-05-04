import psutil
import platform
from datetime import datetime


def compute(res, suffix="B"):
    base = 1024
    for i in ["", "K", "M", "G", "T"]:
        if res < base:
            return f"{res:.2f}{i}{suffix}"
        res = res / base


class CPU:
    def get_no_cores(self):
        cores = psutil.cpu_count()
        return cores

    def usage_per_core(self):
        usages = []
        usage_per_core = {}
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            usage_per_core = {i: percentage}
            usages.append(usage_per_core)

        return usages

    def total_cpu_usage(self):
        return psutil.cpu_percent()


class Memory:
    def memory_details(self):
        comp_memory = psutil.virtual_memory()
        total_memory = compute(comp_memory.total)
        available_memory = compute(comp_memory.available)
        used_memory = compute(comp_memory.used)
        percentage = comp_memory.percent

        results = {
            "Percentage": percentage,
            "Total": total_memory,
            "Available": available_memory,
            "Used": used_memory,
        }

        return results


class Disk:
    def get_disk_details(self):
        partitions = psutil.disk_partitions()
        for part in partitions[:1]:
            mountpoint = part.mountpoint
            disk_usage = psutil.disk_usage(mountpoint)

            used_percentage = disk_usage.percent
            total_disk_size = compute(disk_usage.total)
            free_disk_space = compute(disk_usage.free)

            results = {
                "Used": used_percentage,
                "Total": total_disk_size,
                "Free": free_disk_space,
            }

            return results


class Network:
    def network_details(self):
        network = psutil.net_io_counters()
        bytes_sent = compute(network.bytes_sent)
        bytes_received = compute(network.bytes_recv)
        packets_sent = compute(network.packets_sent)
        packets_recv = compute(network.packets_recv)

        results = {
            "Bytes Sent": bytes_sent,
            "Bytes Received": bytes_received,
            "Packets Sent": packets_sent,
            "Packets Received": packets_recv,
        }

        return results


class NetworkAddress:
    def traffic_details(self):
        net_interface = psutil.net_if_addrs()
        addresses = []
        netmask = []
        broadcast = []
        ptp = []
        all_addresses = []

        for key, value in net_interface.items():
            for item in value:
                if str(item.family) == "AddressFamily.AF_INET":
                    addresses.append(item.address)
                    netmask.append(item.netmask)
                    broadcast.append(item.broadcast)
                    ptp.append(item.ptp)
                results = {
                    "Interface": key,
                    "IP Addresses": addresses,
                    "Netmask": netmask,
                    "Broadcast": broadcast,
                    "Ptp": ptp,
                }
            all_addresses.append(results)
        return all_addresses


class LoadAverage:
    def get_load_averages(self):
        loads = psutil.getloadavg()
        return loads
