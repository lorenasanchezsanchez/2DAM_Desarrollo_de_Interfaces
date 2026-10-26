
from pathlib import Path
import re
import yaml

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

# Ruta del archivo de navegación.
NAV_FILE = Path("docs/apunts/.nav.yml")

# Carpeta donde se generarán los archivos Markdown.
OUTPUT_DIR = Path("docs/apunts/03.2_jetpackcompose/tutorials")

# Dominio de los tutoriales externos.
EXTERNAL_DOMAIN = "https://lawer.github.io/tutorials-pmdm/docs/compose-multiplatform/"

# ==========================================================
# FUNCIONES
# ==========================================================

def slugify(text):
    """Convierte un título en un nombre de archivo seguro."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\-]+", "-", text, flags=re.UNICODE)
    return text.strip("-")


def extract_links(data, links=None):
    """
    Recorre recursivamente el menú YAML y extrae:
    - El título de cada enlace externo.
    - Su URL.
    """
    if links is None:
        links = []

    if isinstance(data, dict):
        for title, value in data.items():
            if isinstance(value, str) and value.startswith(
                "https://lawer.github.io/tutorials-pmdm/"
            ):
                links.append((str(title), value))
            else:
                extract_links(value, links)

    elif isinstance(data, list):
        for item in data:
            extract_links(item, links)

    return links


def create_markdown(title, url):
    """Genera el contenido Markdown con el iframe."""
    return f'''# {title}

<div class="external-page-container">
  <iframe
    src="{url}"
    title="{title}"
    class="external-page-frame"
    loading="lazy">
  </iframe>
</div>
'''


# ==========================================================
# PROCESO PRINCIPAL
# ==========================================================

def main():
    if not NAV_FILE.exists():
        print(f"ERROR: No se encuentra {NAV_FILE.resolve()}")
        print("Ejecuta el script desde la raíz del proyecto MkDocs.")
        return

    # Leer la navegación existente.
    with NAV_FILE.open("r", encoding="utf-8") as file:
        navigation = yaml.safe_load(file)

    # Extraer los enlaces externos.
    links = extract_links(navigation)

    if not links:
        print("No se han encontrado enlaces externos de Compose Multiplatform.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Evitar nombres repetidos.
    used_names = set()
    created = 0

    for title, url in links:
        # Utilizar el nombre del archivo de la URL cuando sea posible.
        filename = Path(url.split("?")[0]).stem

        if not filename or filename == "index":
            filename = slugify(title)

        original_filename = filename
        counter = 2

        while filename in used_names:
            filename = f"{original_filename}-{counter}"
            counter += 1

        used_names.add(filename)

        output_file = OUTPUT_DIR / f"{filename}.md"
        content = create_markdown(title, url)

        output_file.write_text(content, encoding="utf-8")

        print(f"CREADO: {output_file} <- {url}")
        created += 1

    print()
    print(f"Proceso terminado. Archivos creados: {created}")
    print(f"Carpeta: {OUTPUT_DIR.resolve()}")
    print()
    print("Ahora debes actualizar .nav.yml para utilizar estos archivos.")


if __name__ == "__main__":
    main()

