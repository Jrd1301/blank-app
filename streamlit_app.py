import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate projections
def generate_dynamic_projection(current_age, starting_cost, increment_years, growth_rate, years_to_project):
    years = list(range(2024, 2024 + years_to_project + 1, increment_years))
    ages = [current_age + (year - 2024) for year in years]
    costs = [starting_cost * ((1 + growth_rate) ** ((year - 2024))) for year in years]
    projections = {"Age": ages, "Year": years, "Projected Cost ($)": costs}
    return pd.DataFrame(projections)

# Streamlit App Title
st.title("Dynamic Funeral Cost Projection")

# User Inputs
current_age = st.number_input("Enter Current Age:", min_value=0, max_value=120, value=55)
starting_cost = st.number_input("Enter Starting Funeral Cost ($):", min_value=0, value=15000)
growth_rate = st.slider("Annual Growth Rate (%):", min_value=0.0, max_value=10.0, value=4.0) / 100
increment_years = st.slider("Projection Interval (Years):", min_value=1, max_value=10, value=5)
years_to_project = st.slider("Years to Project:", min_value=5, max_value=100, value=60)

# Generate Projection Data
projections_df = generate_dynamic_projection(
    current_age, starting_cost, increment_years, growth_rate, years_to_project
)

# Display Dataframe
st.subheader("Projection Table")
st.dataframe(projections_df)

# Plot the Projection
st.subheader("Projection Chart")
plt.figure(figsize=(10, 6))
plt.plot(projections_df["Year"], projections_df["Projected Cost ($)"], marker='o', label="Funeral Cost")
for i, row in projections_df.iterrows():
    plt.text(row["Year"], row["Projected Cost ($)"], f"Age {row['Age']}", fontsize=8, ha='center')
plt.title(f"Funeral Cost Projections (Starting Age: {current_age})")
plt.xlabel("Year")
plt.ylabel("Projected Cost ($)")
plt.xticks(projections_df["Year"])
plt.legend()
plt.grid(True)
st.pyplot(plt)