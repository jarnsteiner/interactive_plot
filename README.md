# Interactive Activity Plot
von Laurence Bichlbauer und Jan Arnsteiner

Diese Streamlit-App visualisiert Aktivitätsdaten aus einer CSV-Datei.  
Es werden Herzfrequenz und Leistung über die Zeit dargestellt. Zusätzlich werden Herzfrequenzzonen basierend auf der maximalen Herzfrequenz berechnet und im Plot farbig angezeigt.

## Funktionen

- CSV-Daten laden
- Herzfrequenz und Leistung interaktiv darstellen
- Herzfrequenzzonen berechnen
- Zonen farbig im Plot anzeigen
- Durchschnittliche Leistung und Zeit pro Zone als Tabelle anzeigen

## Projekt starten

Zuerst die Abhängigkeiten installieren:

```bash
pdm install
```

App starten mit:
```bash
streamlit run .\main.py
