import psutil
import time
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text

console = Console()


def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return cpu_percent, ram.percent, disk.percent

def display_info():
    while True:
        cpu, ram, disk = get_system_info()

        console.clear()
        console.print(Panel(Text("📊 [bold]Système Monitoring[/bold] 📊", justify="center"), expand=False))

        with Progress() as progress:
            cpu_task = progress.add_task("[cyan]CPU Usage", total=100)
            ram_task = progress.add_task("[magenta]RAM Usage", total=100)
            disk_task = progress.add_task("[yellow]Disk Usage", total=100)

            progress.update(cpu_task, completed=cpu)
            progress.update(ram_task, completed=ram)
            progress.update(disk_task, completed=disk)

            time.sleep(1)

if __name__ == "__main__":
    display_info()
