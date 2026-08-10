# -*- coding: utf-8 -*-
"""Baut eine HTML-Seite mit Gmail-Compose-Links für alle Händleranfragen."""
from urllib.parse import quote
import html

OUT = "/home/user/aktien-cockpit/Fresca-Projekt/07_Mails_abschicken.html"

SIG_DE = """
Mit freundlichen Grüßen
Maximilian Kampits
maximilian.kampits03@gmail.com
Tel.: +43 660 6000226"""

SIG_ES = """
Un cordial saludo,
Maximilian Kampits
maximilian.kampits03@gmail.com
Tel.: +43 660 6000226"""


def de_body(frage1=None):
    f1 = frage1 or "1. Führen Sie dieses Produkt aktuell?"
    return f"""Sehr geehrte Damen und Herren,

ich suche das Erfrischungsgetränk Fresca Toronja von Coca-Cola – und zwar die lateinamerikanische Variante MIT ZUCKER, wie sie in Costa Rica, Honduras oder Mexiko verkauft wird.

Wichtig: Es geht mir ausdrücklich NICHT um die US-Version ("Fresca Zero Sugar" bzw. "Sparkling Soda Water"), die zuckerfrei ist. Die richtige Variante erkennt man an zwei Dingen:
- Der Strichcode beginnt mit 744 (Costa Rica) oder 750 (Mexiko).
- In der Zutatenliste steht "azúcares (azúcar)", nicht "sin azúcar".

Meine Fragen:

{f1}
2. Falls nein: Können Sie es über Ihren Großhändler bestellen?
3. Ich bräuchte idealerweise ein 24er-Gebinde (Dosen 354/355 ml) oder entsprechend 600-ml-Flaschen. Was wäre der Preis?
4. Falls unklar ist, welche Variante Sie führen: Könnten Sie mir ein Foto der Zutatenliste und des Strichcodes schicken?

Ich benötige das Getränk als Geschmacksreferenz für ein Produktentwicklungsprojekt und werde voraussichtlich mehrfach bestellen.

Über eine kurze Rückmeldung freue ich mich. Gerne auch telefonisch.
{SIG_DE}"""


SUBJ_DE = "Anfrage: Fresca Toronja (Zuckervariante) – Verfügbarkeit oder Bestellung"

CASA_F1 = ("1. Führen Sie dieses Produkt aktuell? Ich habe gesehen, dass Sie Jarritos im "
           "Sortiment haben – womöglich läuft Fresca über denselben Lieferanten.")

ES_AMERICANMARKET = f"""Buenos días,

les escribo desde Austria. Me interesa pedir una caja de 24 unidades de Fresca Toronja 355 ml que aparece en su tienda mayorista (distribucionamericanmarket.es).

Es importante: busco la versión latinoamericana CON AZÚCAR, no la versión estadounidense "sin azúcar" / "Zero Sugar". La versión correcta se reconoce por el código de barras que empieza por 744 (Costa Rica) o 750 (México), y por la lista de ingredientes que incluye "azúcares (azúcar)".

Mis preguntas:

1. ¿Tienen stock actualmente?
2. ¿Realizan envíos a Austria? ¿Cuál sería el coste y el plazo de entrega?
3. ¿Cuál sería el precio total de una caja de 24 unidades con el envío incluido?
4. ¿Podrían enviarme una foto de la lista de ingredientes y del código de barras para confirmar que se trata de la versión con azúcar?

Necesito el producto como referencia de sabor para un proyecto de desarrollo de producto, por lo que probablemente repetiré el pedido.

Muchas gracias de antemano.
{SIG_ES}"""

ES_JOTAJOTA = f"""Buenos días,

les escribo desde Austria. Busco el refresco Fresca Toronja de Coca-Cola, concretamente la versión latinoamericana CON AZÚCAR (Costa Rica, Honduras o México). En su web he visto "Gaseosa Fresca Toronja 354 ml".

NO busco la versión estadounidense "sin azúcar" / "Zero Sugar". La versión correcta se reconoce por el código de barras que empieza por 744 o 750, y por la lista de ingredientes que incluye "azúcares (azúcar)".

Mis preguntas:

1. ¿Venden también a clientes particulares, o solo a empresas?
2. ¿Cuál sería el pedido mínimo? Me interesaría una caja de 24 unidades.
3. ¿Realizan envíos a Austria? ¿Coste y plazo de entrega?
4. ¿Podrían confirmarme con una foto de la lista de ingredientes y del código de barras que es la versión con azúcar?

Necesito el producto como referencia de sabor para un proyecto de desarrollo de producto y probablemente repetiré el pedido.

Muchas gracias.
{SIG_ES}"""

ES_CAPRICHOS = f"""Buenos días,

les escribo desde Austria. Busco el refresco Fresca Toronja de Coca-Cola en su versión centroamericana CON AZÚCAR. He visto en su tienda la botella de 2 litros.

NO busco la versión estadounidense "sin azúcar" / "Zero Sugar".

Mis preguntas:

1. ¿Tienen stock actualmente? ¿Disponen también del formato en lata de 354/355 ml?
2. He leído que realizan envíos a toda la Unión Europea. ¿Confirman el envío a Austria? ¿Coste y plazo?
3. Me interesaría una cantidad equivalente a unas 24 latas. ¿Precio total con envío?
4. ¿Podrían enviarme una foto de la lista de ingredientes y del código de barras?

Necesito el producto como referencia de sabor para un proyecto de desarrollo de producto.

Muchas gracias.
{SIG_ES}"""

ES_AMERICACENTRAL = f"""Buenos días,

les escribo desde Austria. Busco la "Gaseosa Fresca Toronja 354 ml" que aparece en su tienda — la versión centroamericana CON AZÚCAR, no la estadounidense "sin azúcar".

Mis preguntas:

1. ¿Tienen stock actualmente?
2. ¿Realizan envíos a Austria? ¿Coste y plazo de entrega?
3. Me interesaría una caja de 24 unidades. ¿Precio total con envío?
4. ¿Podrían enviarme una foto de la lista de ingredientes y del código de barras para confirmar la versión?

Necesito el producto como referencia de sabor para un proyecto de desarrollo de producto.

Muchas gracias.
{SIG_ES}"""

SUBJ_ES_AM = "Consulta: Fresca Toronja con azúcar, caja de 24 – envío a Austria"
SUBJ_ES_JJ = "Consulta: Fresca Toronja con azúcar – envío a Austria"
SUBJ_ES_CC = "Consulta: Fresca Toronja – envío a Austria"
SUBJ_ES_AC = "Consulta: Gaseosa Fresca Toronja – envío a Austria"

# (Name, Ort/Detail, E-Mail oder None, Betreff, Text, Kontaktseite falls keine Mail)
SHOPS = [
    ("Wien", [
        ("Exotic Green", "Meiselmarkt, 1150 Wien · ☎ +43 1 982 03 69",
         "office@exotic-green.at", SUBJ_DE, de_body(), None),
        ("Prosi Exotic Supermarket", "Wimbergergasse 5, 1070 Wien · ☎ +43 1 974 44 44",
         "office@prosi.at", SUBJ_DE, de_body(), None),
        ("Casa México", "Siebensterngasse 16, 1070 Wien · ☎ +43 1 315 45 39",
         "info@casamexico.at", SUBJ_DE, de_body(CASA_F1), None),
        ("MTC Exotic Supermarket", "Kagraner Platz 47 / Stättermayergasse 19",
         "mtc.supermarket.vienna@gmail.com", SUBJ_DE, de_body(), None),
    ]),
    ("Spanien", [
        ("Distribución AmericanMarket", "24er-Gebinde, ca. 26,86 € — die wichtigste Anfrage",
         "ventas@americanmarket.es", SUBJ_ES_AM, ES_AMERICANMARKET, None),
        ("Jota Jota Foods", "Importeur, Valencia",
         "info@jotajotafoods.com", SUBJ_ES_JJ, ES_JOTAJOTA, None),
        ("Caprichos Catrachos", "Madrid — einzige Quelle mit belegter EU-Lieferung",
         None, SUBJ_ES_CC, ES_CAPRICHOS, "https://www.caprichoscatrachos.com/contacto/"),
        ("América Central", "Spanien, Schwerpunkt Zentralamerika",
         None, SUBJ_ES_AC, ES_AMERICACENTRAL, "https://americacentral.es/"),
    ]),
]


def gmail_link(to, subject, body):
    base = "https://mail.google.com/mail/?view=cm&fs=1"
    if to:
        base += f"&to={quote(to)}"
    base += f"&su={quote(subject)}&body={quote(body)}"
    return base


cards = []
for region, shops in SHOPS:
    cards.append(f'<h2>{region}</h2>')
    for name, detail, mail, subj, body, contact in shops:
        link = gmail_link(mail, subj, body)
        if mail:
            addr = f'<code>{html.escape(mail)}</code>'
            note = ""
        else:
            addr = '<span class="warn">Adresse noch holen</span>'
            note = (f'<p class="note">Keine E-Mail-Adresse gefunden — hol sie über '
                    f'<a href="{contact}" target="_blank" rel="noopener">die Kontaktseite</a> '
                    f'und trag sie im Gmail-Fenster oben ein. Betreff und Text sind schon drin.</p>')
        cards.append(f"""
<div class="card">
  <div class="head">
    <div>
      <div class="name">{html.escape(name)}</div>
      <div class="detail">{html.escape(detail)}</div>
      <div class="addr">{addr}</div>
    </div>
    <a class="btn" href="{link}" target="_blank" rel="noopener">In Gmail öffnen →</a>
  </div>
  {note}
  <details>
    <summary>Text ansehen</summary>
    <div class="subj"><strong>Betreff:</strong> {html.escape(subj)}</div>
    <pre>{html.escape(body)}</pre>
  </details>
</div>""")

page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fresca — Händleranfragen abschicken</title>
<style>
  :root {{
    --bg: #f6f7f9; --card: #ffffff; --ink: #14171a; --muted: #6b7280;
    --line: #e3e6ea; --navy: #1f3864; --accent: #1f3864; --warn: #c00000;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #14171a; --card: #1c2024; --ink: #e8eaed; --muted: #9aa3ad;
      --line: #2b3138; --navy: #7ea2e0; --accent: #2d5fb0; --warn: #ff8080;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 28px 18px 60px; background: var(--bg); color: var(--ink);
    font: 15px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  }}
  .wrap {{ max-width: 820px; margin: 0 auto; }}
  h1 {{ font-size: 25px; margin: 0 0 6px; letter-spacing: -.3px; }}
  .lead {{ color: var(--muted); margin: 0 0 26px; }}
  h2 {{
    font-size: 13px; text-transform: uppercase; letter-spacing: .10em;
    color: var(--navy); margin: 34px 0 12px; padding-bottom: 7px;
    border-bottom: 1px solid var(--line);
  }}
  .steps {{
    background: var(--card); border: 1px solid var(--line); border-radius: 10px;
    padding: 16px 20px; margin-bottom: 8px;
  }}
  .steps ol {{ margin: 0; padding-left: 20px; }}
  .steps li {{ margin: 5px 0; }}
  .card {{
    background: var(--card); border: 1px solid var(--line); border-radius: 10px;
    padding: 16px 18px; margin-bottom: 12px;
  }}
  .head {{ display: flex; gap: 16px; align-items: flex-start; justify-content: space-between; flex-wrap: wrap; }}
  .name {{ font-weight: 650; font-size: 16.5px; }}
  .detail {{ color: var(--muted); font-size: 13.5px; margin-top: 2px; }}
  .addr {{ margin-top: 7px; font-size: 13px; }}
  code {{ background: rgba(127,127,127,.14); padding: 2px 6px; border-radius: 4px; font-size: 12.5px; }}
  .warn {{ color: var(--warn); font-weight: 600; font-size: 13px; }}
  .btn {{
    flex-shrink: 0; background: var(--accent); color: #fff; text-decoration: none;
    padding: 10px 17px; border-radius: 7px; font-weight: 600; font-size: 14px;
    white-space: nowrap;
  }}
  .btn:hover {{ filter: brightness(1.12); }}
  .note {{ font-size: 13.5px; color: var(--warn); margin: 12px 0 0; }}
  .note a {{ color: inherit; }}
  details {{ margin-top: 13px; }}
  summary {{ cursor: pointer; color: var(--muted); font-size: 13.5px; }}
  .subj {{ font-size: 13.5px; margin: 11px 0 8px; }}
  pre {{
    white-space: pre-wrap; word-wrap: break-word; background: var(--bg);
    border: 1px solid var(--line); border-radius: 7px; padding: 13px;
    font: 12.5px/1.5 ui-monospace, "SF Mono", Menlo, Consolas, monospace; margin: 0;
    overflow-x: auto;
  }}
  .check {{
    background: var(--card); border: 1px solid var(--line); border-left: 3px solid var(--warn);
    border-radius: 10px; padding: 15px 19px; margin-top: 30px;
  }}
  .check h3 {{ margin: 0 0 8px; font-size: 15px; }}
  table {{ border-collapse: collapse; margin-top: 9px; font-size: 14px; }}
  td {{ padding: 4px 14px 4px 0; }}
  td:first-child {{ font-weight: 650; font-family: ui-monospace, Menlo, monospace; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>Händleranfragen abschicken</h1>
  <p class="lead">Acht Anfragen nach Fresca Toronja — der Zuckervariante. Ein Klick öffnet
  Gmail mit Empfänger, Betreff und Text schon ausgefüllt.</p>

  <div class="steps">
    <ol>
      <li>Auf <strong>„In Gmail öffnen"</strong> klicken — ein neuer Tab geht auf.</li>
      <li>Text kurz überfliegen.</li>
      <li>Senden. Zurück zu dieser Seite, nächster Laden.</li>
    </ol>
  </div>
  <p class="lead" style="margin:12px 0 0;font-size:13.5px;">Alle acht am selben Tag rausschicken.
  Du brauchst nur einen Treffer, weißt aber vorher nicht, welcher es wird.</p>

  {"".join(cards)}

  <div class="check">
    <h3>Worauf du bei den Antworten achtest</h3>
    <p style="margin:0;font-size:14px;">Die entscheidende Rückmeldung ist das <strong>Foto vom
    Strichcode</strong>. „Ja, haben wir" meint oft die US-Version — die ist in Europa
    verbreiteter. Ohne Foto keine Bestellung.</p>
    <table>
      <tr><td>744</td><td>Costa Rica — genau dein Original ✅</td></tr>
      <tr><td>750</td><td>Mexiko — auch Zucker, passt ✅</td></tr>
      <tr><td>0</td><td>USA, zuckerfrei — ablehnen ❌</td></tr>
    </table>
    <p style="margin:12px 0 0;font-size:14px;">Wer nach 5 Werktagen nicht antwortet: bei den
    Wienern anrufen. Nummern stehen oben bei jedem Laden.</p>
  </div>
</div>
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(page)
print("gespeichert:", OUT, len(page), "Zeichen")
