# main.py
import argparse
import requests  # Importamos la nueva librería
from src.converter import html_to_markdown

def main():
    """
    Punto de entrada para la herramienta de web scraping y conversión a Markdown.
    """
    parser = argparse.ArgumentParser(
        description="Extrae el contenido de una URL y lo convierte a Markdown.",
        epilog="Ejemplo: python main.py https://example.com salida.md --ignore-class 'ad'"
    )
    
    # --- CAMBIO #1: Cambiamos 'input_file' por 'url' ---
    parser.add_argument(
        "url",
        help="La URL completa de la página web a procesar."
    )
    parser.add_argument(
        "output_file",
        help="La ruta al archivo Markdown de salida."
    )
    parser.add_argument(
        "--ignore-class",
        nargs='+',
        metavar='CSS_CLASS',
        default=[],
        help="Una o más clases CSS a ignorar durante la conversión."
    )

    args = parser.parse_args()

    # --- CAMBIO #2: Reemplazamos la lectura de archivo por una petición web ---
    try:
        print(f"🕸️  Obteniendo HTML desde: {args.url}")
        
        # Añadimos un User-Agent para simular un navegador y evitar bloqueos simples
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        response = requests.get(args.url, headers=headers, timeout=10)
        # Esto lanzará un error si la página devolvió un código de error (ej. 404, 500)
        response.raise_for_status()
        
        # Obtenemos el contenido HTML de la respuesta
        html_content = response.text
            
        print("✅ HTML obtenido correctamente.")
        
        # Guardamos el contenido HTML sin procesar en un archivo separado
        raw_html_file = args.output_file.replace('.md', '_raw.html')
        with open(raw_html_file, 'w', encoding='utf-8') as raw_file:
            raw_file.write(html_content)
        print(f"🌐 Contenido HTML sin procesar guardado en: {raw_html_file}")
        
        # El resto del código no cambia. La función de conversión se usa igual.
        print("DEBUG: Calling html_to_markdown with arguments:")
        print(f"HTML Content: {html_content[:100]}...")  # Print first 100 characters for brevity
        print(f"Ignore Classes: {args.ignore_class}")
        markdown_output = html_to_markdown(
            html_content=html_content
        )

        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_output)
            
        print(f"🚀 Conversión exitosa. Archivo guardado en: {args.output_file}")
        if args.ignore_class:
            print(f"ℹ️  Clases ignoradas: {', '.join(args.ignore_class)}")

    # Añadimos un manejo de errores específico para 'requests'
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de red o HTTP al intentar acceder a la URL: {e}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()
