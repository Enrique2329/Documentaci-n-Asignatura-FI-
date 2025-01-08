# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
def skip_main_code(app, what, name, obj, skip, options):
    """
    Esta función se usa para evitar que se ejecute el código bajo `if __name__ == "__main__"`
    cuando se usa Sphinx para documentar el módulo.
    """
    if name == "__main__":
        return True
    return skip

# Conectar la función a la configuración de Sphinx para evitar la ejecución del código
def setup(app):
    app.connect('autodoc-skip-member', skip_main_code)
    
latex_documents = [
    ('index', 'Documentacion.tex', u'Documentacion de cuaderno de practicas', u'Enrique Gómez', 'manual'),
]


project = 'Enrique Gómez'
copyright = '2025, enrique'
author = 'enrique'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = []
extensions = [
'sphinx.ext.autodoc',
'sphinx.ext.viewcode',
'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
