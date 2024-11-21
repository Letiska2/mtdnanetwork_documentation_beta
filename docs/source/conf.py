# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mtDNA-Network'
copyright = '2024, leticia'
author = 'leticia'
release = '2.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
# html_logo = "_static/favicon.png"  # Caminho para a logo
# html_theme_options = {
#   #  "sidebar_hide_name": True,  # Esconde o nome do projeto na barra lateral
#     "light_css_variables": {
#         "color-brand-primary": "MediumSeaGreen",
#         "color-brand-content": "BlueViolet",
#         "color-brand-background": "Salmon"
#     },
#     "dark_css_variables": {
#         "color-brand-primary": "SpringGreen",
#         "color-brand-content": "BlueViolet",
#         "color-brand-background": "Fuchsia"
#     },
# }

html_theme_options = {
    "light_css_variables": {
        "image-network": "_static/star_import.png",
        # Cores de marcação primária e de conteúdo 
        "color-code-foreground": "#343242",      
        "color-brand-primary": "MediumSeaGreen", #  Verde piscina (links, botões)
        "color-brand-content": "BlueViolet", # Lilás pastel (texto de links ativos)
        "color-brand-background": "Salmon",
        # Fundo da página e fundo do conteúdo principal
        "color-background-primary": "#FFFFFF",     # Cor de fundo principal da página (branco)
        "color-background-secondary": "#F7F7F7",   # Cor de fundo da seção de conteúdo (cinza claro)

        # Texto e títulos
        "color-text-primary": "#343242",           # Cor do texto principal (preto)
        "color-text-secondary": "#343242",         # Cor de texto secundário e texto menor (cinza escuro)
        "color-text-title": "#343242",             # Cor dos títulos e subtítulos (cinza médio)

        # Cores para notas (important, tip, note, etc.)
        "color-admonition-title--important": "#D32F2F",  # Título para nota de "importante" (vermelho)
        "color-admonition-title--note": "#0288D1",       # Título para nota de "nota" (azul)
        "color-admonition-title--tip": "#388E3C",        # Título para nota de "dica" (verde)
        "color-admonition-title--warning": "#FBC02D",    # Título para nota de "aviso" (amarelo)

        # Fundo e borda das notas
        "color-admonition-background--important": "#FFEBEE",  # Fundo da nota "importante" (rosa claro)
        "color-admonition-background--note": "BlueViolet",       # Fundo da nota "nota" (azul claro)
        "color-admonition-background--tip": "#E8F5E9",        # Fundo da nota "dica" (verde claro)
        "color-admonition-background--warning": "#FFF8E1",    # Fundo da nota "aviso" (bege claro)
        "color-border": "#E0E0E0",                            # Cor de borda (cinza claro)

        # Código e blocos de código
        "color-background-code": "#F5F2F0",         # Fundo de blocos de código (cinza muito claro)
        "color-text-code": "#D6336C",               # Texto do código inline (rosa)
        "color-border-code": "#CCCCCC",             # Borda de blocos de código (cinza)

        # Rodapé
        "color-background-footer": "#212121",       # Fundo do rodapé (preto)
        "color-text-footer": "#BDBDBD",             # Texto do rodapé (cinza claro)
    },
    "dark_css_variables": {
        "image-network": "_static/star.png",
        # Cores de marcação primária e de conteúdo
        "color-brand-primary": "SpringGreen",
        "color-brand-content": "BlueViolet",
        "color-brand-background": "Fuchsia",

        # Fundo da página e fundo do conteúdo principal
        "color-background-primary": "#121212",      # Cor de fundo principal da página (quase preto)
        "color-background-secondary": "#1E1E1E",    # Cor de fundo da seção de conteúdo (cinza escuro)

        # Texto e títulos
        "color-text-primary": "#FFFFFF",            # Cor do texto principal (branco)
        "color-text-secondary": "#BBBBBB",          # Cor de texto secundário e texto menor (cinza claro)
        "color-text-title": "#E0E0E0",              # Cor dos títulos e subtítulos (cinza claro)

        # Cores para notas (important, tip, note, etc.)
        "color-admonition-title--important": "#FF1744",  # Título para nota de "importante" (vermelho vibrante)
        "color-admonition-title--note": "#40C4FF",       # Título para nota de "nota" (azul vibrante)
        "color-admonition-title--tip": "#00E676",        # Título para nota de "dica" (verde vibrante)
        "color-admonition-title--warning": "#FFC107",    # Título para nota de "aviso" (amarelo vibrante)

        # Fundo e borda das notas
        "color-admonition-background--important": "#FF5252",  # Fundo da nota "importante" (vermelho claro)
        "color-admonition-background--note": "#80D8FF",       # Fundo da nota "nota" (azul claro vibrante)
        "color-admonition-background--tip": "#B9FBC0",        # Fundo da nota "dica" (verde claro vibrante)
        "color-admonition-background--warning": "#FFE57F",    # Fundo da nota "aviso" (amarelo claro)
        "color-border": "#424242",                            # Cor de borda (cinza escuro)

        # Código e blocos de código
        "color-background-code": "#2E2E2E",         # Fundo de blocos de código (cinza escuro)
        "color-text-code": "#FF4081",               # Texto do código inline (rosa vibrante)
        "color-border-code": "#757575",             # Borda de blocos de código (cinza médio)

        # Rodapé
        "color-background-footer": "#1C1C1C",       # Fundo do rodapé (cinza escuro)
        "color-text-footer": "#E0E0E0",             # Texto do rodapé (cinza claro)
    },
    "light_logo": "logol.png",   # Logo para o modo claro # type: ignore
    "dark_logo": "logod.png",    # Logo para o modo escuro 
 #   "logo_link": "http://gilbioinfo.pythonanywhere.com/",  # Link para a ferramenta   
}


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

pygments_style = 'sphinx'


html_theme = 'furo' # alabaster #furo
html_static_path = ['_static']
html_css_files = ["custom.css"]
