```python
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

class SEOForecastApp:
    def __init__(self):
        st.set_page_config(
            page_title="SEO Forecast",
            page_icon="📈",
            layout="wide"
        )
        
    def run(self):
        self.render_sidebar()
        self.render_header()
        self.render_main_content()

    def render_sidebar(self):
        with st.sidebar:
            st.title("⚙️ Configuration")
            
            # Configuration des sources
            st.header("Sources de données")
            
            # Google Search Console
            with st.expander("Google Search Console"):
                st.file_uploader("Importer données GSC", type=['csv'])
                st.text_input("API Key GSC")
                
            # Google Analytics
            with st.expander("Google Analytics"):
                st.file_uploader("Importer données GA4", type=['csv'])
                st.text_input("API Key GA4")
            
            # Paramètres de prévision
            st.header("Paramètres")
            forecast_period = st.selectbox(
                "Période de prévision",
                ["3 mois", "6 mois", "12 mois"]
            )
            
            confidence_level = st.slider(
                "Niveau de confiance",
                min_value=0.8,
                max_value=0.99,
                value=0.95,
                step=0.01
            )

    def render_header(self):
        col1, col2, col3 = st.columns([2,1,1])
        
        with col1:
            st.title("SEO Forecast 📈")
        
        with col2:
            st.button("Rafraîchir les données", type="primary")
            
        with col3:
            st.download_button(
                "Exporter les résultats",
                data="",  # À remplacer par les données réelles
                file_name="seo_forecast.csv",
                mime="text/csv"
            )

    def render_main_content(self):
        # KPIs
        self.render_kpis()
        
        # Graphiques
        col1, col2 = st.columns(2)
        
        with col1:
            self.render_traffic_forecast()
            
        with col2:
            self.render_revenue_forecast()
            
        # Tableau d'opportunités
        self.render_opportunities_table()

    def render_kpis(self):
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        with kpi1:
            self.metric_card(
                "Trafic Organique",
                "125,000",
                "+15.4%",
                "prévision: 145,000"
            )
            
        with kpi2:
            self.metric_card(
                "Revenu SEO",
                "250,000 €",
                "+22.7%",
                "prévision: 310,000 €"
            )
            
        with kpi3:
            self.metric_card(
                "Taux de Conversion",
                "2.8%",
                "-0.3%",
                "prévision: 3.2%"
            )
            
        with kpi4:
            self.metric_card(
                "ROI SEO",
                "285%",
                "+12.5%",
                "prévision: 320%"
            )

    def metric_card(self, title, value, change, forecast):
        st.metric(
            label=title,
            value=value,
            delta=change,
            help=forecast
        )

    def render_traffic_forecast(self):
        st.subheader("Prévision de Trafic")
        
        # Données simulées
        dates = pd.date_range(start='2024-01-01', periods=180, freq='D')
        actual = np.random.normal(1000, 100, 90)
        forecast = np.random.normal(1200, 150, 90)
        
        fig = go.Figure()
        
        # Données réelles
        fig.add_trace(go.Scatter(
            x=dates[:90],
            y=actual,
            name="Réel",
            line=dict(color='#1d4ed8', width=2)
        ))
        
        # Prévisions
        fig.add_trace(go.Scatter(
            x=dates[90:],
            y=forecast,
            name="Prévision",
            line=dict(color='#60a5fa', dash='dash')
        ))
        
        st.plotly_chart(fig, use_container_width=True)

    def render_revenue_forecast(self):
        st.subheader("Prévision de Revenu")
        
        # Données simulées
        dates = pd.date_range(start='2024-01-01', periods=180, freq='D')
        revenue = np.random.normal(5000, 500, 180)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=revenue,
            name="Revenu",
            line=dict(color='#059669')
        ))
        
        st.plotly_chart(fig, use_container_width=True)

    def render_opportunities_table(self):
        st.subheader("Opportunités SEO")
        
        # Données simulées
        data = {
            'Mot-clé': ['mot clé 1', 'mot clé 2', 'mot clé 3'],
            'Position': [8, 6, 5],
            'Volume': [12000, 8000, 6500],
            'Difficulté': [35, 42, 28],
            'Potentiel': [85, 75, 90]
        }
        
        df = pd.DataFrame(data)
        
        # Affichage avec mise en forme
        st.dataframe(
            df,
            column_config={
                "Potentiel": st.column_config.ProgressColumn(
                    "Potentiel",
                    help="Potentiel d'amélioration",
                    format="%d%%",
                    min_value=0,
                    max_value=100,
                ),
            },
            hide_index=True,
        )

if __name__ == "__main__":
    app = SEOForecastApp()
    app.run()
```