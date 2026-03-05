# Munih Hava Durumu

Munih icin anlık hava durumunu terminalde gosteren Python CLI uygulamasi.

## Ozellikler

- Sicaklik, nem, ruzgar hizi ve hava durumu aciklamasi
- Renkli terminal ciktisi (rich kutuphanesi)
- Ucretsiz Open-Meteo API (key gerektirmez)

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanim

```bash
python weather.py
```

## Ornek Cikti

```
╭─────────────────── Munih Hava Durumu ───────────────────╮
│                                                          │
│   Durum        Kismen bulutlu                            │
│   Sicaklik     8 °C                                      │
│   Nem          72%                                       │
│   Ruzgar Hizi  14 km/h                                   │
│   Guncelleme   2026-03-05T12:00                          │
│                                                          │
│                    Kaynak: Open-Meteo                    │
╰──────────────────────────────────────────────────────────╯
```

## API

[Open-Meteo](https://open-meteo.com/) — ucretsiz, kayit gerektirmeyen hava durumu API'si.
