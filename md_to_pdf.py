#!/usr/bin/env python3
"""
Convierte el informe final de defensa (Markdown) a PDF usando WeasyPrint.
Uso: python md_to_pdf.py
"""

import markdown
import os
import sys

# Intentar importar weasyprint
try:
    from weasyprint import HTML
except ImportError:
    print("Error: weasyprint no esta instalado. Ejecuta: pip install weasyprint")
    sys.exit(1)

# Intentar importar markdown, si no esta, usar mistune
try:
    import markdown as md_lib
    USE_MARKDOWN = True
except ImportError:
    USE_MARKDOWN = False

if not USE_MARKDOWN:
    try:
        import mistune
        USE_MISTUNE = True
    except ImportError:
        print("Error: Se necesita 'markdown' o 'mistune'. Ejecuta: pip install markdown")
        sys.exit(1)
else:
    USE_MISTUNE = False


def md_to_html(md_text):
    """Convierte markdown a HTML."""
    if USE_MARKDOWN:
        html = md_lib.markdown(
            md_text,
            extensions=["tables", "fenced_code", "toc", "nl2br"]
        )
    else:
        html = mistune.html(md_text)
    return html


def build_full_html(body_html, title="Informe Final de Proyecto y Defensa"):
    """Envuelve el HTML del body con estructura completa y estilos CSS."""
    css = """
    @page {
        size: A4;
        margin: 2cm 2.5cm;
        @bottom-center {
            content: counter(page);
            font-size: 9pt;
            color: #666;
        }
    }

    body {
        font-family: 'DejaVu Sans', 'Liberation Sans', Arial, Helvetica, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #1a1a1a;
        max-width: 100%;
    }

    h1 {
        font-size: 22pt;
        color: #1a3c5e;
        border-bottom: 3px solid #1a3c5e;
        padding-bottom: 8px;
        margin-top: 30px;
        margin-bottom: 15px;
        page-break-after: avoid;
    }

    h2 {
        font-size: 16pt;
        color: #2c5f8a;
        border-bottom: 1.5px solid #ccc;
        padding-bottom: 5px;
        margin-top: 25px;
        margin-bottom: 12px;
        page-break-after: avoid;
    }

    h3 {
        font-size: 13pt;
        color: #3a7ab5;
        margin-top: 20px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }

    h4 {
        font-size: 11.5pt;
        color: #4a8ac5;
        margin-top: 15px;
        margin-bottom: 8px;
        page-break-after: avoid;
    }

    p {
        margin-bottom: 8px;
        text-align: justify;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin: 12px 0;
        font-size: 10pt;
        page-break-inside: avoid;
    }

    th {
        background-color: #2c5f8a;
        color: white;
        padding: 8px 10px;
        text-align: left;
        font-weight: bold;
        border: 1px solid #1a3c5e;
    }

    td {
        padding: 6px 10px;
        border: 1px solid #ddd;
    }

    tr:nth-child(even) {
        background-color: #f5f8fb;
    }

    tr:hover {
        background-color: #e8f0f8;
    }

    code {
        background-color: #f0f0f0;
        padding: 2px 5px;
        border-radius: 3px;
        font-family: 'DejaVu Sans Mono', 'Liberation Mono', monospace;
        font-size: 9.5pt;
    }

    pre {
        background-color: #f5f5f5;
        padding: 12px;
        border-radius: 5px;
        border-left: 4px solid #2c5f8a;
        overflow-x: auto;
        font-size: 9pt;
        line-height: 1.4;
        page-break-inside: avoid;
    }

    pre code {
        background: none;
        padding: 0;
    }

    img {
        max-width: 85%;
        display: block;
        margin: 15px auto;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 4px;
    }

    em {
        color: #555;
        font-size: 9.5pt;
    }

    blockquote {
        border-left: 4px solid #2c5f8a;
        margin: 12px 0;
        padding: 8px 15px;
        background-color: #f5f8fb;
        color: #333;
    }

    strong {
        color: #1a3c5e;
    }

    hr {
        border: none;
        border-top: 2px solid #2c5f8a;
        margin: 25px 0;
    }

    ul, ol {
        margin-bottom: 10px;
        padding-left: 25px;
    }

    li {
        margin-bottom: 4px;
    }

    /* Portada */
    .cover-page {
        text-align: center;
        padding-top: 120px;
        page-break-after: always;
    }

    .cover-page h1 {
        font-size: 28pt;
        color: #1a3c5e;
        border: none;
        margin-bottom: 20px;
    }

    .cover-page h2 {
        font-size: 18pt;
        color: #2c5f8a;
        border: none;
        font-weight: normal;
    }

    .cover-page .subtitle {
        font-size: 14pt;
        color: #555;
        margin-top: 40px;
    }

    .cover-page .info {
        font-size: 12pt;
        color: #666;
        margin-top: 60px;
        line-height: 2;
    }
    """

    cover_page = """
    <div class="cover-page">
        <h1>Informe Final de Proyecto y Defensa</h1>
        <h2>Analisis de Datos Oncologicos del Registro Institucional de Tumores de Argentina (RITA 2012-2022)</h2>
        <div class="subtitle">
            Aplicacion de Tecnicas de Machine Learning No Supervisado
        </div>
        <div class="info">
            <p><strong>Materia:</strong> Machine Learning</p>
            <p><strong>Universidad Nacional de San Agustin (UNSA)</strong></p>
        </div>
    </div>
    """

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
    {css}
    </style>
</head>
<body>
    {cover_page}
    {body_html}
</body>
</html>"""

    return full_html


def main():
    # Rutas
    base_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(base_dir, "reports")
    md_file = os.path.join(reports_dir, "00_PROYECTO_FINAL_DE_DEFENSA.md")
    pdf_file = os.path.join(reports_dir, "PROYECTO_FINAL_DE_DEFENSA.pdf")

    # Verificar que el archivo markdown existe
    if not os.path.exists(md_file):
        print(f"Error: No se encontro el archivo {md_file}")
        sys.exit(1)

    print(f"Leyendo: {md_file}")

    # Leer el markdown
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    print("Convirtiendo Markdown a HTML...")
    body_html = md_to_html(md_text)

    print("Construyendo documento HTML completo con estilos...")
    full_html = build_full_html(body_html)

    print(f"Generando PDF: {pdf_file}")

    # Generar PDF con WeasyPrint
    html_obj = HTML(
        string=full_html,
        base_url=reports_dir  # Para que las rutas relativas de imagenes funcionen
    )
    html_obj.write_pdf(pdf_file)

    # Verificar el resultado
    if os.path.exists(pdf_file):
        size_mb = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"PDF generado exitosamente: {pdf_file}")
        print(f"Tamano: {size_mb:.2f} MB")
    else:
        print("Error: No se pudo generar el PDF")
        sys.exit(1)


if __name__ == "__main__":
    main()
