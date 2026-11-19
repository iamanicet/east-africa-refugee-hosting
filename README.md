# Refugee Hosting in East Africa

Which East African countries host the most refugees, and who carries the heaviest burden relative to their population? An analysis of UNHCR and World Bank data, 2010 to 2025, with an interactive dashboard. Built with Python, pandas, Plotly and Streamlit.

Live app: ([link added after deployment](https://east-africa-refugee-hosting-wyusqrnzayuvlzf6y796xn.streamlit.app/))

![Dashboard showing refugees per 1,000 inhabitants in East Africa, 2025](app-ranking.png)

## Summary

- Uganda hosts the most refugees in the region (about 1.9 million), but South Sudan carries the heaviest burden per person: 49.4 refugees per 1,000 inhabitants in 2025.
- Adjusting for population changes the ranking. Ethiopia falls from 2nd by count to 8th per 1,000 inhabitants, while Djibouti rises from 9th to 3rd.
- Kenya's asylum seekers more than tripled between 2022 and 2024, from about 69,000 to about 220,000.

## The question

Headlines about displacement give large numbers but little sense of who carries the burden. This project asks:

1. Which East African countries host the most refugees, and how has this changed since 2010?
2. How does the picture change once refugee numbers are adjusted for population size?

## Key findings (2025)

- Uganda hosts the most refugees in the region (about 1.9 million), followed by Ethiopia (about 1.0 million) and Sudan (about 810,000).
- Per 1,000 inhabitants, South Sudan (49.4) and Uganda (37.7) carry the heaviest burden, followed by Djibouti (21.0) and Sudan (15.7). That is roughly 1 refugee for every 20 residents in South Sudan, 1 in 27 in Uganda and 1 in 93 in Kenya.
- The ranking changes once population is taken into account. Ethiopia drops from 2nd by count to 8th per 1,000 inhabitants (7.5), while Djibouti rises from 9th to 3rd and South Sudan from 5th to 1st.
- Kenya hosts about 617,000 refugees (4th by count, 5th per 1,000 inhabitants at 10.7). Its refugee numbers peaked in 2011 (about 566,000), fell to about 421,000 by 2018, then climbed steadily.
- Kenya's asylum seekers rose from about 69,000 in 2022 to about 153,000 in 2023 and about 220,000 in 2024, more than tripling in two years.
- Countries moved in very different directions: Uganda grew steadily, Tanzania and Rwanda peaked in the mid-2010s and declined, Burundi and South Sudan rose sharply in recent years, and Eritrea fell to near zero.

## Implications

1. Report refugee burden per capita alongside raw counts. Population-adjusted figures reveal pressure that headline totals hide, as in South Sudan and Djibouti.
2. Monitor Kenya's asylum-seeker numbers, which more than tripled between 2022 and 2024. The data shows that it happened, not why, so the drivers should be investigated.
3. Report refugees and internally displaced people separately, since this analysis excludes internally displaced people.

## Data sources

- UNHCR Population Statistics API: refugees and asylum seekers by country of asylum, 2010 onward.
- World Bank, total population (indicator SP.POP.TOTL).

Data retrieved in November 2026. Data is from public sources and is credited to UNHCR and the World Bank. Please check each source's terms of use before reusing the data.

## Method

1. Retrieve refugee data for 11 East African countries from the UNHCR API.
2. Retrieve total population for the same countries from the World Bank API.
3. Clean the data (convert text values to numbers, standardize country names).
4. Merge both sources on country and year.
5. Calculate refugees per 1,000 inhabitants = refugees / population x 1,000.
6. Compare country rankings by raw count and by population-adjusted burden.
7. Present the results in an interactive Streamlit dashboard.

## Project structure

- analysis.ipynb: the full analysis, step by step
- app.py: the Streamlit dashboard
- data/raw: World Bank population files downloaded by the notebook
- data/processed: the merged dataset used by the app
- images: screenshots used in this README
- requirements.txt: Python libraries needed

## Run it locally

    pip install -r requirements.txt
    streamlit run app.py

## Limitations

- Only refugees hosted are counted. Internally displaced people are not included, although they make up a large share of displacement in countries such as Sudan, South Sudan, Ethiopia and Somalia.
- National figures hide local pressure. Refugees are usually concentrated in particular districts or camps.
- Population is not the same as capacity to host. Countries differ in income and resources.
- The analysis shows what changed, not why. Explaining the trends needs conflict, policy and funding data.
- Population figures are estimates and may be revised.
- The most recent refugee figures may be provisional, so trends end in 2025.
- South Sudan has no record before 2011, the year it became independent.
- The set of countries is a working definition of East Africa.

## Next steps

- Add internally displaced people to the analysis.
- Add GDP per capita to compare burden with capacity to host.
- Use subnational and camp-level data (UNHCR Kenya operational portal) to look at local pressure.
- Bring in conflict and policy data to explain the trends.

## Author

Anicet Baraka Ciza

GitHub: iamanicet
LinkedIn: linkedin.com/in/anicetbarakaciza
