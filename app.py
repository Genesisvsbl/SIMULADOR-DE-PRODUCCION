from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Productividad Planta",
    page_icon="P",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .stApp {
        background: #eef3f6;
      }

      [data-testid="stHeader"],
      [data-testid="stToolbar"] {
        background: transparent;
      }

      .block-container {
        max-width: 100vw !important;
        padding: 0 !important;
      }

      iframe {
        display: block;
        width: 100vw !important;
        min-width: 100vw !important;
      }

      [data-testid="stVerticalBlock"],
      [data-testid="stVerticalBlockBorderWrapper"],
      .element-container {
        width: 100% !important;
        max-width: 100% !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "outputs" / "simulador_productividad_planta.html"

if not html_path.exists():
    st.error("No se encontro el simulador HTML.")
else:
    html = html_path.read_text(encoding="utf-8")
    components.html(html, height=1250, scrolling=True)
