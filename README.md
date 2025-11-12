# Helligkeit-Farben-berechnen

Ein Script zur Bestimmung der hellsten Farbe aus einer Liste von Hexadezimal-Farbwerten.

## 📋 Beschreibung

Dieses Projekt analysiert eine Liste von Farben (als Hexadezimalwerte) und identifiziert die hellste Farbe. Das Script gibt die RGB-Komponenten der hellsten Farbe aus.

## 🎯 Ziel

Das Script soll:
- Die hellste Farbe aus einer Liste von Hexadezimal-Farbwerten auswählen
- Die RGB-Komponenten (Rot, Grün, Blau) einzeln ausgeben
- **Bonus:** Den Namen der Farbe über die [CSS Colors API](https://www.csscolorsapi.com/) ermitteln

## 🏗️ Funktionsweise

### 1. Eingabe
Das Script erhält eine Liste von Hexadezimal-Farbwerten

### 2. Verarbeitung
- Konvertierung der Hexadezimalwerte in RGB-Komponenten
- Berechnung der Helligkeit jeder Farbe
- Identifikation der hellsten Farbe

### 3. Ausgabe
- Aus der Liste wird die hellste Farbe im hexadecimal und rgb Format benannt und mit Namen versehen.

## 💡 Beispiel

### Eingabe:
```python
list = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
```

### Ausgabe mit Farbnamen:
```
The brightest color is: #FFFFFF (r=255, g=255, b=255), called 'White'
```

## 📸 Screenshot

<img width="500" height="221" alt="Beispielausgabe des Scripts" src="https://github.com/user-attachments/assets/587e03eb-1201-46e7-abef-259d0a062548" />

