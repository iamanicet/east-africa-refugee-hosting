"""
East Africa refugee hosting dashboard.

Reads the processed file created in the notebook
(data/processed/east_africa_refugees_population.csv) and lets the viewer
explore refugee counts and refugees per 1,000 inhabitants.

Run locally:
    pip install streamlit pandas plotly
    streamlit run app.py
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = Path(__file__).parent / "data" / "processed" / "east_africa_refugees_population.csv"

st.set_page_config(page_title="Refugee Hosting in East Africa", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)


df = load_data()

# Years where population is available, so per-capita figures can be calculated
years_with_population = sorted(df.dropna(subset=["population"])["year"].unique())
latest_year = int(max(years_with_population))
countries = sorted(df["coa_name"].unique())

st.title("Refugee Hosting in East Africa")
st.write(
    "Who hosts refugees, and who carries the heaviest burden relative to population? "
    "Raw counts and population-adjusted figures tell different stories."
)

# ---- Sidebar controls ----
st.sidebar.header("Controls")
year = st.sidebar.selectbox(
    "Year", [int(y) for y in reversed(years_with_population)], index=0
)
measure = st.sidebar.radio(
    "Measure", ["Refugees per 1,000 inhabitants", "Number of refugees"]
)
selected = st.sidebar.multiselect("Countries (for trends)", countries, default=countries)

measure_col = "refugees_per_1000" if measure.startswith("Refugees per") else "refugees"

tab_rank, tab_trend, tab_compare, tab_about = st.tabs(
    ["Ranking", "Trends", "Rank comparison", "About the data"]
)

# ---- Tab 1: ranking for the chosen year ----
with tab_rank:
    snapshot = df[df["year"] == year].sort_values(measure_col, ascending=True)
    fig = px.bar(
        snapshot,
        x=measure_col,
        y="coa_name",
        orientation="h",
        text_auto=".2s" if measure_col == "refugees" else ".1f",
        title=f"{measure}, {year}",
        labels={measure_col: measure, "coa_name": "Country"},
        height=500,
    )
    st.plotly_chart(fig)

# ---- Tab 2: trends over time ----
with tab_trend:
    trend = df[(df["coa_name"].isin(selected)) & (df["year"] <= latest_year)]
    fig = px.line(
        trend,
        x="year",
        y=measure_col,
        color="coa_name",
        markers=True,
        title=f"{measure}, 2010 to {latest_year}",
        labels={"year": "Year", measure_col: measure, "coa_name": "Country"},
        height=500,
    )
    st.plotly_chart(fig)
    st.caption(
        "Per-1,000 figures are only available for years with World Bank population data."
    )

# ---- Tab 3: how the ranking changes once population is considered ----
with tab_compare:
    table = df[df["year"] == year][
        ["coa_name", "refugees", "population", "refugees_per_1000"]
    ].copy()
    table["rank_by_count"] = table["refugees"].rank(ascending=False).astype(int)
    table["rank_per_1000"] = table["refugees_per_1000"].rank(ascending=False).astype(int)
    table["rank_change"] = table["rank_by_count"] - table["rank_per_1000"]
    table = table.sort_values("rank_per_1000").rename(
        columns={
            "coa_name": "Country",
            "refugees": "Refugees",
            "population": "Population",
            "refugees_per_1000": "Refugees per 1,000",
            "rank_by_count": "Rank by count",
            "rank_per_1000": "Rank per 1,000",
            "rank_change": "Rank change",
        }
    )
    st.write(
        f"Rank change is positive when a country moves up once population is taken "
        f"into account ({year})."
    )
    st.dataframe(table.round(1), hide_index=True)

# ---- Tab 4: method and limitations ----
with tab_about:
    st.markdown(
        """
**Sources**
- UNHCR Population Statistics API (refugees and asylum seekers by country of asylum)
- World Bank, total population (indicator SP.POP.TOTL)

**Method**
Refugees per 1,000 inhabitants = refugees hosted / total population x 1,000.

**Limitations**
- Only refugees hosted are counted. Internally displaced people are not included.
- Population figures are estimates and may be revised.
- The most recent refugee figures may be provisional.
- South Sudan has no record before 2011, the year it became independent.
- Countries included are a working definition of East Africa.
"""
    )