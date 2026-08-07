# -*- coding: utf-8 -*-
"""Druckfertiger Blindverkostungsbogen (A4)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

OUT = "/home/user/aktien-cockpit/Fresca-Projekt/03_Blindverkostung_Bogen.pdf"

NAVY = colors.HexColor("#1F3864")
LIGHT = colors.HexColor("#D9E2F3")
GREY = colors.HexColor("#808080")
LINE = colors.HexColor("#BFBFBF")

CODES = [
    ("471", "Referenz"),
    ("628", "Probe 2"),
    ("359", "Probe 3"),
    ("815", "Probe 4"),
]

H1 = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=16, textColor=colors.white,
                    leading=20, spaceAfter=0)
H2 = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=11, textColor=NAVY,
                    leading=14, spaceBefore=8, spaceAfter=4)
BODY = ParagraphStyle("BODY", fontName="Helvetica", fontSize=9.5, leading=13.5)
SMALL = ParagraphStyle("SMALL", fontName="Helvetica", fontSize=8, leading=11, textColor=GREY)
WARN = ParagraphStyle("WARN", fontName="Helvetica-Bold", fontSize=9.5, leading=13,
                      textColor=colors.HexColor("#C00000"))
CODEST = ParagraphStyle("CODE", fontName="Helvetica-Bold", fontSize=15, textColor=NAVY,
                        leading=18)

story = []


def banner(text):
    t = Table([[Paragraph(text, H1)]], colWidths=[175 * mm], rowHeights=[13 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t


def checkbox(size=4.2):
    """Ein echtes leeres Ankreuzkästchen — als Rahmen gezeichnet, nicht als Zeichen.
    Helvetica hat kein U+25A1; das würde als schwarzer Block gedruckt."""
    b = Table([[""]], colWidths=[size * mm], rowHeights=[size * mm])
    b.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.7, NAVY)]))
    return b


def writeline(label=None, width=175):
    """Eine Schreiblinie (echte Linie statt Unterstrich-Kette)."""
    t = Table([[Paragraph(label, BODY) if label else ""]],
              colWidths=[width * mm], rowHeights=[7 * mm])
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return t


def scale_row(label, lo, hi, n, start=1):
    """Eine Skalenzeile mit ankreuzbaren Kästchen."""
    digits = [str(i) for i in range(start, start + n)]
    inner = Table([digits], colWidths=[6.6 * mm] * n, rowHeights=[6.6 * mm])
    inner.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.6, NAVY),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONT", (0, 0), (-1, -1), "Helvetica", 8.5),
        ("TEXTCOLOR", (0, 0), (-1, -1), GREY),
    ]))
    row = Table(
        [[Paragraph(f"<b>{label}</b>", BODY), Paragraph(lo, SMALL), inner, Paragraph(hi, SMALL)]],
        colWidths=[34 * mm, 20 * mm, (6.6 * n + 1) * mm, 20 * mm])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ]))
    return row


def sample_block(code, pos):
    head = Table([[Paragraph(f"PROBE {pos}", ParagraphStyle(
        "p", fontName="Helvetica-Bold", fontSize=9, textColor=colors.white)),
        Paragraph(f"CODE {code}", ParagraphStyle(
            "c", fontName="Helvetica-Bold", fontSize=13, textColor=colors.white,
            alignment=2))]],
        colWidths=[80 * mm, 95 * mm], rowHeights=[7.5 * mm])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    comment = Table([[Paragraph("<b>Was fällt dir auf?</b>", BODY), writeline(width=132)]],
                    colWidths=[34 * mm, 133 * mm])
    comment.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    inner = Table([[scale_row("Gesamteindruck", "schlecht", "sehr gut", 10)],
                   [scale_row("Süße", "zu wenig", "zu süß", 9)],
                   [comment]], colWidths=[175 * mm])
    inner.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ]))
    return KeepTogether([head, inner, Spacer(1, 2.5 * mm)])


# ============================================================ SEITE 1
story.append(banner("BLINDVERKOSTUNG — ANLEITUNG FÜR DICH"))
story.append(Spacer(1, 3 * mm))
story.append(Paragraph(
    "Diese Seite ist <b>nur für dich als Organisator</b>. Sie enthält die Auflösung der "
    "Blindcodes — kopiere sie niemals für die Teilnehmer mit.", WARN))
story.append(Spacer(1, 3 * mm))

story.append(Paragraph("WAS DU BRAUCHST", H2))
for t in [
    "4 identische, undurchsichtige Becher pro Teilnehmer — gleiche Form, gleiche Farbe.",
    "Einen wasserfesten Stift. Nur der dreistellige Code kommt auf den Becher, sonst nichts.",
    "Stilles Wasser und neutrale Cracker oder Weißbrot zum Neutralisieren.",
    "Alle Proben auf gleicher Temperatur, ca. 7–8 °C. Temperaturunterschiede verfälschen das Ergebnis stärker als jede Rezepturänderung.",
    "Einen ausgedruckten Bogen (Seite 2) je Teilnehmer.",
]:
    story.append(Paragraph(f"• {t}", BODY))

story.append(Paragraph("ABLAUF", H2))
for i, t in enumerate([
    "Becher außer Sichtweite der Teilnehmer einschenken.",
    "Die Reihenfolge bei jedem Teilnehmer wechseln — sonst bevorzugt allein die Position eine Probe.",
    "Nichts über die Proben sagen. Kein „das ist meins“, kein „das ist das Original“. Ein einziger Hinweis kippt das Ergebnis.",
    "Zwischen den Proben Wasser und einen Bissen Brot.",
    "Bogen vollständig ausfüllen lassen, bevor der nächste Teilnehmer kommt.",
    "Erst wenn alle Bögen ausgefüllt sind, die Codes auflösen.",
    "Zahlen in die Excel-Mappe eintragen: Blatt „Verkostung“, ab Zeile 30.",
]):
    story.append(Paragraph(f"<b>{i+1}.</b> {t}", BODY))

story.append(Paragraph("DAS MACHT DAS ERGEBNIS WERTLOS", H2))
for t in [
    "Freunde, die wissen, welche Probe von dir ist.",
    "Unterschiedliche Temperatur oder Kohlensäure zwischen den Proben.",
    "Weniger als 30 Teilnehmer — darunter ist der Zufall größer als der Unterschied.",
    "Verkosten nach dem Essen, mit Kaffee oder direkt nach dem Zähneputzen.",
]:
    story.append(Paragraph(f"• {t}", WARN))

story.append(Paragraph("BLINDCODES — AUFLÖSUNG", H2))
legend = [["Code", "Was tatsächlich im Becher ist"]] + [
    ["471", "Referenz — Fresca Original (Import aus Spanien oder Costa Rica)"],
    ["628", "Variante A — Vollzucker, ca. 10 g/100 ml, kein Süßstoff"],
    ["359", "Variante B — Fresca-Original nachgebaut, ca. 6 g Zucker + Süßstoff"],
    ["815", "Variante C — nur Zucker, ca. 6 g/100 ml, kein Süßstoff"],
]
t = Table(legend, colWidths=[22 * mm, 153 * mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9),
    ("FONT", (0, 1), (0, -1), "Helvetica-Bold", 10),
    ("FONT", (1, 1), (1, -1), "Helvetica", 9),
    ("GRID", (0, 0), (-1, -1), 0.5, LINE),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
]))
story.append(t)
story.append(Spacer(1, 4 * mm))
story.append(Paragraph(
    "<b>Entscheidungsregel, die du vorher festlegst:</b> Schlägt keine eigene Variante die "
    "Referenz (471) um mindestens 0,5 Punkte im Gesamteindruck, ist die Rezeptur noch nicht "
    "fertig — dann geht eine weitere Musterschleife ans Aromahaus. Diese Regel jetzt "
    "festlegen, nicht nachher. Sonst redest du dir das Ergebnis schön.", BODY))

story.append(PageBreak())

# ============================================================ SEITE 2
story.append(banner("BLINDVERKOSTUNG — GRAPEFRUIT-LIMONADE"))
story.append(Spacer(1, 3 * mm))

limo = Table([[Paragraph("<b>Trinkst du Limo?</b>", BODY),
               checkbox(3.6), Paragraph("oft", BODY),
               checkbox(3.6), Paragraph("selten", BODY),
               checkbox(3.6), Paragraph("nie", BODY)]],
             colWidths=[27 * mm, 5 * mm, 9 * mm, 5 * mm, 13 * mm, 5 * mm, 8 * mm])
limo.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                          ("LEFTPADDING", (0, 0), (-1, -1), 1),
                          ("RIGHTPADDING", (0, 0), (-1, -1), 1)]))

meta = Table([[
    Paragraph("<b>Teilnehmer-Nr.</b>  ______", BODY),
    Paragraph("<b>Datum</b>  __________", BODY),
    Paragraph("<b>Alter</b>  ______", BODY),
    limo,
]], colWidths=[36 * mm, 38 * mm, 23 * mm, 78 * mm])
meta.setStyle(TableStyle([
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
]))
story.append(meta)
story.append(Spacer(1, 2.5 * mm))
story.append(Paragraph(
    "Probiere die vier Proben in der angegebenen Reihenfolge. Trink zwischendurch etwas "
    "Wasser. Kreuze in jeder Zeile eine Zahl an. Es gibt keine richtige Antwort — "
    "dein spontaner Eindruck zählt.", BODY))
story.append(Spacer(1, 2.5 * mm))

for i, (code, _) in enumerate(CODES):
    story.append(sample_block(code, i + 1))

story.append(Spacer(1, 1 * mm))
final_head = Table([[Paragraph(
    "ZUM SCHLUSS", ParagraphStyle("f", fontName="Helvetica-Bold", fontSize=10,
                                  textColor=colors.white))]],
    colWidths=[175 * mm], rowHeights=[8 * mm])
final_head.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#C00000")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(final_head)

cells = []
for c, _ in CODES:
    cells += [checkbox(5), Paragraph(f"<b>{c}</b>", CODEST)]
boxes = Table([cells], colWidths=[7 * mm, 34 * mm] * 4, rowHeights=[9 * mm])
boxes.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 1),
    ("RIGHTPADDING", (0, 0), (-1, -1), 1),
]))

final = Table([
    [Paragraph("<b>Welche Probe würdest du dir im Laden kaufen?</b>  (nur eine ankreuzen)", BODY)],
    [boxes],
    [writeline("<b>Warum genau die?</b>", 168)],
    [writeline(None, 168)],
    [writeline("<b>Was hätte keine der Proben, das du dir wünschen würdest?</b>", 168)],
    [writeline(None, 168)],
], colWidths=[175 * mm])
final.setStyle(TableStyle([
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 1),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
]))
story.append(final)
story.append(Spacer(1, 1.5 * mm))
story.append(Paragraph("Danke! Bitte den Bogen abgeben, ohne ihn mit anderen zu besprechen.",
                       SMALL))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(18 * mm, 10 * mm, "Fresca-Projekt — Blindverkostung")
    canvas.drawRightString(192 * mm, 10 * mm, f"Seite {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=17 * mm,
                        topMargin=14 * mm, bottomMargin=16 * mm,
                        title="Blindverkostung Grapefruit-Limonade",
                        author="Fresca-Projekt")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("gespeichert:", OUT)
