import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="SEO Forecast",
    page_icon="📈",
    layout="wide"
)

# Configuration style
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Titre principal
st.title("SEO Forecast 📈")

# Sidebar avec menu de configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    with st.expander("🔗 Sources de données"):
        uploaded_file_gsc = st.file_uploader(
            "Données Search Console (CSV)",
            type=['csv']
        )
        uploaded_file_ga = st.file_uploader(
            "Données Analytics (CSV)",
            type=['csv']
        )
    
    periode = st.selectbox(
        "📅 Période de prévision",
        ["3 mois", "6 mois", "12 mois"]
    )
    
    confidence = st.slider(
        "🎯 Niveau de confiance",
        min_value=80,
        max_value=99,
        value=95,
        help="Niveau de confiance des prévisions"
    )
    
    st.button("🔄 Actualiser les prévisions", type="primary")

# KPIs principaux
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Trafic Organique",
        value="125,000",
        delta="15.4%",
        help="Trafic organique mensuel"
    )

with col2:
    st.metric(
        label="Revenu SEO",
        value="250,000 €",
        delta="22.7%",
        help="Revenu généré par le trafic organique"
    )

with col3:
    st.metric(
        label="Conversion",
        value="2.8%",
        delta="-0.3%",
        help="Taux de conversion moyen"
    )

with col4:
    st.metric(
        label="ROI SEO",
        value="285%",
        delta="12.5%",
        help="Retour sur investissement SEO"
    )

# Graphiques
tab1, tab2 = st.tabs(["📈 Prévisions", "🎯 Opportunités"])

with tab1:
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("Prévision de Trafic")
        dates = pd.date_range(start='2024-01-01', periods=90)
        data = np.random.normal(1000, 100, 90)
        df = pd.DataFrame({
            'date': dates,
            'traffic': data
        })
        st.line_chart(df.set_index('date'))
    
    with chart_col2:
        st.subheader("Prévision de Revenu")
        revenue_data = data * 10  # Simulation de revenu
        df_revenue = pd.DataFrame({
            'date': dates,
            'revenue': revenue_data
        })
        st.line_chart(df_revenue.set_index('date'))

with tab2:
    st.subheader("Opportunités SEO")
    
    # Données d'exemple pour le tableau d'opportunités
    opportunities = pd.DataFrame({
        'Mot-clé': ['chaussures running', 'baskets sport', 'running femme'],
        'Position': [8, 6, 5],
        'Volume': [12000, 8000, 6500],
        'Potentiel': [85, 75, 90]
    })
    
    st.dataframe(
        opportunities,
        column_config={
            "Potentiel": st.column_config.ProgressColumn(
                "Potentiel",
                help="Potentiel d'amélioration",
                format="%d%%",
                min_value=0,
                max_value=100,
            )
        },
        hide_index=True
    )