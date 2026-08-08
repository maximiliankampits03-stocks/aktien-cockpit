# -*- coding: utf-8 -*-
"""Einseitiges Lastenheft als PDF-Anhang für Aromahaus und Lohnabfüller."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle)

OUT = "/home/user/aktien-cockpit/Fresca-Projekt/01b_Lastenheft_Anhang.pdf"

NAVY = colors.HexColor("#1F3864")
LIGHT = colors.HexColor("#D9E2F3")
GREY = colors.HexColor("#808080")
LINE = colors.HexColor("#BFBFBF")

H1 = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=15, textColor=colors.white, leading=19)
H2 = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=10.5, textColor=NAVY,
                    leading=14, spaceBefore=9, spaceAfter=3)
BODY = ParagraphStyle("BODY", fontName="Helvetica", fontSize=9, leading=12.5)
CELL = ParagraphStyle("CELL", fontName="Helvetica", fontSize=8.5, leading=11.5)
CELLB = ParagraphStyle("CELLB", fontName="Helvetica-Bold", fontSize=8.5, leading=11.5)
SMALL = ParagraphStyle("SMALL", fontName="Helvetica", fontSize=7.5, leading=10, textColor=GREY)

story = []

t = Table([[Paragraph("LASTENHEFT — ZUCKERREDUZIERTE GRAPEFRUIT-LIMONADE", H1)]],
          colWidths=[175 * mm], rowHeights=[12 * mm])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY),
                       ("LEFTPADDING", (0, 0), (-1, -1), 8),
                       ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
story.append(t)
story.append(Spacer(1, 2 * mm))
story.append(Paragraph(
    "Projekt: Markteinführung einer eigenen Getränkemarke in Österreich &nbsp;·&nbsp; "
    "Stand: Entwurf zur Bemusterung &nbsp;·&nbsp; Referenzmuster werden beigestellt", SMALL))
story.append(Spacer(1, 3 * mm))


def table(rows, widths, head=True):
    data = []
    for i, r in enumerate(rows):
        style = CELLB if (head and i == 0) else CELL
        data.append([Paragraph(str(c), CELLB if (head and i == 0) else
                               (CELLB if j == 0 and not (head and i == 0) else style))
                     for j, c in enumerate(r)])
    tb = Table(data, colWidths=widths)
    st = [("GRID", (0, 0), (-1, -1), 0.5, LINE),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("TOPPADDING", (0, 0), (-1, -1), 3),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
          ("LEFTPADDING", (0, 0), (-1, -1), 4)]
    if head:
        st += [("BACKGROUND", (0, 0), (-1, 0), NAVY),
               ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
               ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT])]
    tb.setStyle(TableStyle(st))
    return tb


story.append(Paragraph("1. GESCHMACKSZIEL", H2))
story.append(Paragraph(
    "Trockene, leicht bittere Grapefruit-Citrus-Note. Deutlich weniger süß als "
    "marktübliche Grapefruit-Limonaden, klar bis leicht trüb, ohne Farbstoff. "
    "Als Referenz wird <b>Fresca (lateinamerikanische Rezeptur, zuckerhaltig)</b> "
    "beigestellt. Ziel ist ein eigenständiges Produkt mit diesem Geschmacksprofil — "
    "keine Kopie.", BODY))

story.append(Paragraph("2. ZIELWERTE FERTIGGETRÄNK", H2))
story.append(table([
    ["Parameter", "Zielwert", "Bemerkung"],
    ["Zucker", "5–6 g / 100 ml", "bewusst NICHT zuckerfrei — Referenz liegt bei ca. 5,9 g"],
    ["Brennwert", "ca. 24 kcal / 100 ml", "entspricht ca. 79 kcal je 330-ml-Dose"],
    ["Grapefruitsaft a. Konzentrat", "1 % (Variante D: 6 %)", "6-%-Variante zur Prüfung der Bezeichnung „Fruchtlimonade“"],
    ["Süßung", "Zucker, ggf. + Süßstoff", "Vorschlag des Aromahauses erbeten"],
    ["Kohlensäure", "mittel bis hoch", "wie marktübliche Limonade"],
    ["Farbe", "klar, kein Farbstoff", ""],
    ["Konservierung", "Natriumbenzoat oder gleichwertig", "kein Ascorbinsäure-Zusatz (Benzol-Risiko)"],
], [46 * mm, 40 * mm, 89 * mm]))

story.append(Paragraph("3. ZU BEMUSTERNDE VARIANTEN", H2))
story.append(table([
    ["Variante", "Zucker", "Süßstoff", "Saft", "Zweck"],
    ["B", "ca. 6 g/100 ml", "ja (Sucralose + Ace-K)", "1 %", "Nachbau des Referenzprofils"],
    ["C", "ca. 6 g/100 ml", "nein", "1 %", "kürzestmögliche Zutatenliste"],
    ["D", "ca. 6 g/100 ml", "nein", "6 %", "wie C, mit echter Fruchtnote"],
], [18 * mm, 28 * mm, 40 * mm, 15 * mm, 74 * mm]))
story.append(Spacer(1, 1.5 * mm))
story.append(Paragraph(
    "Alle drei Varianten bitte parallel bemustern — sie werden gegen die Referenz "
    "blind verkostet. Eine reine Zero-Variante wird ausdrücklich <b>nicht</b> benötigt.", BODY))

story.append(Paragraph("4. RAHMENBEDINGUNGEN", H2))
story.append(table([
    ["Punkt", "Vorgabe"],
    ["Gebinde", "330 ml Aluminiumdose, Dekor als Shrink-Sleeve auf Blankodose"],
    ["Erstcharge", "20.000 Dosen, Perspektive 100.000+ pro Jahr"],
    ["Zielmarkt", "Österreich, später DACH"],
    ["Recht", "Alle Zutaten müssen in der EU für Erfrischungsgetränke zugelassen und nach VO 1169/2011 kennzeichenbar sein"],
    ["Ausgeschlossen", "E385 (Calcium-Dinatrium-EDTA); E445 nur nach ausdrücklicher Zulässigkeitsprüfung"],
    ["Haltbarkeit", "mindestens 12 Monate ungekühlt"],
], [30 * mm, 145 * mm]))

story.append(Paragraph("5. WORUM WIR BITTEN", H2))
for i, t_ in enumerate([
    "Betreuen Sie Projekte in dieser Größenordnung? Wenn nein: ab welcher Menge?",
    "Welche Entwicklungskosten entstehen, und wie viele Iterationsschleifen sind enthalten?",
    "Wie lange dauert es von der Beauftragung bis zum ersten Muster?",
    "Welche Süßungsstrategie empfehlen Sie für dieses Profil — und warum?",
    "Übernehmen Sie die Prüfung der Zutatenliste auf EU-Konformität?",
]):
    story.append(Paragraph(f"<b>{i+1}.</b> {t_}", BODY))

story.append(Spacer(1, 4 * mm))
story.append(Paragraph(
    "Referenzmuster werden auf Wunsch zugesendet. Für Rückfragen stehen wir jederzeit "
    "zur Verfügung.", BODY))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(18 * mm, 10 * mm, "Lastenheft — zuckerreduzierte Grapefruit-Limonade")
    canvas.drawRightString(192 * mm, 10 * mm, f"Seite {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=17 * mm,
                        topMargin=14 * mm, bottomMargin=16 * mm,
                        title="Lastenheft zuckerreduzierte Grapefruit-Limonade")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("gespeichert:", OUT)
