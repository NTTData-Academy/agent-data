"""Genera los documentos 100% sintéticos del Laboratorio 1.

Todo el contenido (banco, productos, personas, montos, RUC, direcciones) es ficticio.
Uso:  python labs/lab01/scripts/generar_pdfs_sinteticos.py
"""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak)

OUT = Path(__file__).resolve().parents[1] / "data"
OUT.mkdir(exist_ok=True)

ss = getSampleStyleSheet()
H1 = ParagraphStyle("h1", parent=ss["Heading1"], fontSize=16, spaceAfter=6)
H2 = ParagraphStyle("h2", parent=ss["Heading2"], fontSize=12.5, spaceBefore=10, spaceAfter=4)
P = ParagraphStyle("p", parent=ss["BodyText"], fontSize=9.5, leading=13)
SMALL = ParagraphStyle("s", parent=P, fontSize=8, leading=10, textColor=colors.grey)
AVISO = "DOCUMENTO SINTÉTICO — Banco Andino Ficticio no existe. Uso exclusivo para el Laboratorio 1."


def tabla(data, widths, header=True):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
          ("FONTSIZE", (0, 0), (-1, -1), 8.5),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("LEFTPADDING", (0, 0), (-1, -1), 4)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3A5F")),
               ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
               ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]
    t.setStyle(TableStyle(st))
    return t


def pie(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.grey)
    canvas.drawString(1.8 * cm, 1.2 * cm, AVISO)
    canvas.drawRightString(A4[0] - 1.8 * cm, 1.2 * cm, f"Página {doc.page}")
    canvas.restoreState()


def ficha_producto():
    c = lambda s: Paragraph(s, P)
    doc = SimpleDocTemplate(str(OUT / "ficha_tarjetas_credito_banco_andino.pdf"), pagesize=A4,
                            leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm, bottomMargin=2 * cm,
                            title="Ficha de productos: Tarjetas de crédito Cóndor (sintético)")
    s = []
    s += [Paragraph("Banco Andino Ficticio S.A.", SMALL),
          Paragraph("Ficha de producto y guía de atención: Tarjetas de crédito Cóndor", H1),
          Paragraph("Código de documento: BAF-TC-GUIA-007 · Versión 3.2 · Vigencia: 01/10/2026 – 31/03/2027 · "
                    "Área responsable: Gestión de Productos de Tarjetas", SMALL), Spacer(1, 6),
          Paragraph("1. Propósito y alcance", H2),
          Paragraph("Esta guía orienta a los especialistas de negocio en la atención de consultas sobre la familia de "
                    "tarjetas de crédito Cóndor: características, costos, requisitos, procedimientos de solicitud, "
                    "bloqueo y reclamos. Las tasas y comisiones vigentes deben confirmarse siempre en el sistema de "
                    "características de productos; ante una diferencia, prevalece el sistema.", P),
          Paragraph("2. Catálogo de tarjetas", H2),
          tabla([["Tarjeta", "Segmento objetivo", "Línea de crédito (S/)", "Programa de beneficios"],
                 [c("Cóndor Clásica"), c("Primer tarjeta, ingresos desde S/ 1,500"), "1,000 – 8,000", c("1 punto Cumbre por cada S/ 10")],
                 [c("Cóndor Oro"), c("Ingresos desde S/ 3,500"), "8,001 – 25,000", c("1.5 puntos por S/ 10 y seguro de compras")],
                 [c("Cóndor Platinum"), c("Ingresos desde S/ 7,000"), "25,001 – 60,000", c("2 puntos por S/ 10, acceso a salas VIP (4 al año)")],
                 [c("Cóndor Emprende"), c("Personas con negocio (RUC 10)"), "3,000 – 40,000", c("Cashback 1% en proveedores afiliados")]],
                [3.3 * cm, 4.7 * cm, 3.4 * cm, 6 * cm]),
          Paragraph("3. Costos y tarifario referencial", H2),
          tabla([["Concepto", "Clásica", "Oro", "Platinum", "Emprende"],
                 ["Membresía anual", "S/ 0", "S/ 180", "S/ 450", "S/ 120"],
                 ["Exoneración de membresía", c("No aplica"), c("Consumos ≥ S/ 6,000 al año"), c("Consumos ≥ S/ 18,000 al año"), c("Consumos ≥ S/ 4,000 al año")],
                 ["TEA compras (referencial)", "49.9%", "39.9%", "29.9%", "34.9%"],
                 ["TEA disposición de efectivo", "84.9%", "79.9%", "69.9%", "74.9%"],
                 ["Comisión disposición efectivo", "S/ 12.00", "S/ 12.00", "S/ 8.00", "S/ 10.00"],
                 ["Seguro de desgravamen mensual", "0.09% saldo", "0.09% saldo", "0.07% saldo", "0.09% saldo"],
                 ["Reposición de plástico", "S/ 15.00", "S/ 15.00", "S/ 0", "S/ 15.00"]],
                [4.6 * cm, 2.7 * cm, 3.4 * cm, 3.4 * cm, 3.3 * cm]),
          Paragraph("Nota: la TEA (tasa efectiva anual) es referencial. El valor aplicable a cada cliente depende de su "
                    "evaluación crediticia y debe consultarse en el sistema de características de productos.", SMALL),
          PageBreak(),
          Paragraph("4. Requisitos de solicitud", H2),
          tabla([["Requisito", "Dependiente", "Independiente", "Cóndor Emprende"],
                 ["Edad", "21 a 75 años", "21 a 75 años", "21 a 75 años"],
                 [c("Documento de identidad vigente"), "Sí", "Sí", "Sí"],
                 [c("Antigüedad laboral o de negocio"), "6 meses", "12 meses", "12 meses"],
                 [c("Sustento de ingresos"), c("3 últimas boletas de pago"), c("Declaración anual de renta"), c("Ficha RUC activa + 6 últimas declaraciones mensuales")],
                 [c("Calificación en central de riesgos"), "Normal", "Normal", c("Normal o CPP con aval")]],
                [4.6 * cm, 4 * cm, 4 * cm, 4.8 * cm]),
          Paragraph("5. Procedimiento de solicitud (canal agencia)", H2),
          Paragraph("Paso 1. Verificar la identidad del cliente con documento físico y validación biométrica.<br/>"
                    "Paso 2. Consultar la oferta precalificada en el sistema; si no existe, registrar la solicitud para evaluación.<br/>"
                    "Paso 3. Explicar costos, TEA, membresía y condiciones de exoneración antes de la firma.<br/>"
                    "Paso 4. Entregar la Hoja Resumen y el contrato; obtener la firma digital del cliente.<br/>"
                    "Paso 5. Registrar la dirección de entrega. El plástico se entrega en 5 días hábiles (Lima) o 8 días hábiles (provincias).<br/>"
                    "Paso 6. Recordar la activación en la app y la creación de la clave en un cajero o en la app.", P),
          Paragraph("6. Bloqueo por pérdida o robo", H2),
          Paragraph("El cliente puede bloquear la tarjeta en la app (opción Seguridad &gt; Bloquear), en la banca telefónica "
                    "(línea ficticia 01 700-0000, 24 horas) o en agencia. El especialista nunca debe solicitar la clave, "
                    "el CVV ni códigos de verificación. Tras el bloqueo, la reposición se solicita en el mismo acto.", P),
          Paragraph("7. Reclamos y plazos de atención", H2),
          tabla([["Tipo de caso", "Canal de registro", "Plazo máximo de respuesta"],
                 [c("Consumo no reconocido"), c("App, banca telefónica, agencia"), "15 días hábiles"],
                 [c("Cobro indebido de membresía"), c("Agencia, banca telefónica"), "10 días hábiles"],
                 [c("Solicitud de copia de contrato"), c("Agencia, correo de atención"), "7 días hábiles"],
                 [c("Reclamo general (Libro de Reclamaciones)"), c("Agencia, web"), "30 días calendario"]],
                [6.4 * cm, 5.5 * cm, 5.5 * cm]),
          Paragraph("8. Restricciones y buenas prácticas", H2),
          Paragraph("• No ofrecer tasas garantizadas ni aprobaciones sin evaluación crediticia.<br/>"
                    "• No compartir información de otros clientes ni confirmar datos personales por teléfono.<br/>"
                    "• Las disposiciones de efectivo no generan puntos Cumbre.<br/>"
                    "• Los consumos en el extranjero se convierten con el tipo de cambio del día de procesamiento.<br/>"
                    "• Ante dudas no cubiertas por esta guía, derivar a la mesa de ayuda de Productos (anexo ficticio 4521).", P)]
    doc.build(s, onFirstPage=pie, onLaterPages=pie)


def factura():
    doc = SimpleDocTemplate(str(OUT / "factura_sintetica_plasticos_andes.pdf"), pagesize=A4,
                            leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm, bottomMargin=2 * cm,
                            title="Factura electrónica F001-004587 (sintética)")
    s = []
    cab = Table([[Paragraph("<b>Plásticos y Seguridad Andes S.A.C.</b><br/>RUC: 20999888771<br/>"
                            "Av. Los Inventados 742, Lima, Perú<br/>facturacion@plasticos-andes.example", P),
                  Paragraph("<b>FACTURA ELECTRÓNICA</b><br/>N° F001-004587<br/>Fecha de emisión: 15/10/2026<br/>"
                            "Fecha de vencimiento: 14/11/2026", P)]],
                colWidths=[10 * cm, 7.4 * cm])
    cab.setStyle(TableStyle([("BOX", (1, 0), (1, 0), 0.8, colors.HexColor("#1F3A5F")),
                             ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    s += [cab, Spacer(1, 10),
          Paragraph("<b>Cliente:</b> Banco Andino Ficticio S.A.<br/><b>RUC:</b> 20111222333<br/>"
                    "<b>Dirección:</b> Jr. Imaginario 1200, San Isidro, Lima<br/>"
                    "<b>Orden de compra:</b> OC-2026-0931 · <b>Moneda:</b> Soles (PEN) · <b>Condición:</b> Crédito 30 días", P),
          Spacer(1, 10)]
    items = [["Ítem", "Descripción", "Cant.", "Valor unit. (S/)", "Importe (S/)"],
             ["1", "Plástico tarjeta Cóndor Clásica con chip EMV", "5,000", "3.20", "16,000.00"],
             ["2", "Plástico tarjeta Cóndor Oro con chip EMV y contactless", "2,000", "4.10", "8,200.00"],
             ["3", "Plástico tarjeta Cóndor Platinum metálica", "500", "18.50", "9,250.00"],
             ["4", "Personalización y embozado de datos", "7,500", "0.60", "4,500.00"],
             ["5", "Sobre de seguridad para envío", "7,500", "0.35", "2,625.00"]]
    s += [tabla(items, [1.2 * cm, 8.6 * cm, 1.8 * cm, 2.9 * cm, 2.9 * cm]), Spacer(1, 8)]
    tot = Table([["Subtotal (valor de venta)", "S/ 40,575.00"],
                 ["IGV (18%)", "S/ 7,303.50"],
                 ["TOTAL A PAGAR", "S/ 47,878.50"]], colWidths=[5 * cm, 3.4 * cm], hAlign="RIGHT")
    tot.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                             ("FONTNAME", (0, 2), (-1, 2), "Helvetica-Bold"),
                             ("ALIGN", (1, 0), (1, -1), "RIGHT"), ("FONTSIZE", (0, 0), (-1, -1), 9)]))
    s += [tot, Spacer(1, 12),
          Paragraph("<b>Son:</b> cuarenta y siete mil ochocientos setenta y ocho con 50/100 soles.", P),
          Paragraph("<b>Forma de pago:</b> transferencia a la cuenta ficticia 000-0000000-0-00 del Banco Imaginario.", P),
          Spacer(1, 10), Paragraph(AVISO, SMALL)]
    doc.build(s, onFirstPage=pie)


if __name__ == "__main__":
    ficha_producto()
    factura()
    print("PDFs generados en", OUT)
