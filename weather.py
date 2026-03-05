import sys
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

API_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=48.1351&longitude=11.5820"
    "&current=temperature_2m,weathercode,windspeed_10m,relativehumidity_2m"
    "&timezone=Europe%2FBerlin"
)

WMO_CODES = {
    0: "Acik",
    1: "Cok az bulutlu",
    2: "Kismen bulutlu",
    3: "Bulutlu",
    45: "Sisli",
    48: "Kivrimsi sis",
    51: "Hafif cicekli yagmur",
    53: "Orta cicekli yagmur",
    55: "Yogun cicekli yagmur",
    61: "Hafif yagmur",
    63: "Orta yagmur",
    65: "Siddetti yagmur",
    71: "Hafif kar",
    73: "Orta kar",
    75: "Yogun kar",
    80: "Hafif saganak",
    81: "Orta saganak",
    82: "Siddetti saganak",
    95: "Firtina",
    96: "Dolu ile firtina",
    99: "Agir dolu ile firtina",
}


def get_weather_description(code: int) -> str:
    return WMO_CODES.get(code, f"Bilinmeyen ({code})")


def fetch_weather() -> dict:
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Hata: Internet baglantisi kurulamadi.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Hata: Istek zaman asimina ugradi.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"Hata: API yanit hatasi: {e}")
        sys.exit(1)


def main():
    console = Console()

    data = fetch_weather()
    current = data["current"]

    temp = current["temperature_2m"]
    code = current["weathercode"]
    wind = current["windspeed_10m"]
    humidity = current["relativehumidity_2m"]
    time = current["time"]

    description = get_weather_description(code)

    table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    table.add_column("Bilgi", style="bold cyan")
    table.add_column("Deger", style="white")

    table.add_row("Durum", description)
    table.add_row("Sicaklik", f"{temp} °C")
    table.add_row("Nem", f"{humidity}%")
    table.add_row("Ruzgar Hizi", f"{wind} km/h")
    table.add_row("Guncelleme", time)

    panel = Panel(
        table,
        title="[bold yellow]Munih Hava Durumu[/bold yellow]",
        subtitle="[dim]Kaynak: Open-Meteo[/dim]",
        border_style="blue",
        padding=(1, 2),
    )

    console.print(panel)


if __name__ == "__main__":
    main()
