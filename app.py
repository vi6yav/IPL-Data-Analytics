import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="IPL Dashboard", layout="wide")

# ---- CUSTOM THEME ----
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1 {
        color: #FF4D8D;
        text-align: center;
    }

    h2, h3 {
        color: #C77DFF;
    }

    .stMetric {
        background: linear-gradient(135deg, #1E1E2E, #2A2A40);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 0px 10px rgba(199,125,255,0.3);
    }

    hr {
        border: 1px solid #C77DFF;
    }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.title("IPL Data Analytics Dashboard")
st.markdown("### Insights from IPL Matches")

# ---- LOAD DATA ----
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# ---- SIDEBAR FILTER ----
st.sidebar.header("Filter")

teams = matches["winner"].dropna().unique()
selected_team = st.sidebar.selectbox("Select Team", ["All"] + sorted(list(teams)))

if selected_team != "All":
    matches = matches[matches["winner"] == selected_team]

# ---- KPIs ----
col1, col2, col3 = st.columns(3)

col1.metric("Total Matches", len(matches))
col2.metric("Teams", matches["winner"].nunique())
col3.metric("Toss Wins", matches["toss_winner"].nunique())

st.markdown("---")

# ---- TEAM PERFORMANCE + TOSS ----
col1, col2 = st.columns(2)

# Team Performance
with col1:
    st.subheader("Team Performance (Top Winning Teams)")

    team_wins = matches["winner"].value_counts().head(10)

    fig, ax = plt.subplots()
    team_wins.plot(
        kind="bar",
        color="#C77DFF",
        edgecolor="#FF4D8D",
        ax=ax
    )

    plt.xticks(rotation=45)
    plt.ylabel("Wins")
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    st.pyplot(fig)

    st.markdown("*A few teams consistently dominate IPL wins.*")

# Toss Impact
with col2:
    st.subheader("Toss Impact")

    toss = matches[matches["toss_winner"] == matches["winner"]]

    sizes = [len(toss), len(matches) - len(toss)]
    labels = ["Win Toss & Match", "Lose After Toss"]

    fig2, ax2 = plt.subplots()
    ax2.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        colors=["#C77DFF", "#FF4D8D"],
        wedgeprops={"edgecolor": "black"}
    )

    st.pyplot(fig2)

    st.markdown("*Toss gives an advantage but does not guarantee victory.*")

# ---- TOP BATSMEN ----
st.markdown("---")
st.subheader("Top Batsmen")

top_batsmen = deliveries.groupby("batsman")["batsman_runs"].sum().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots()
top_batsmen.plot(kind="bar", color="#FF4D8D", ax=ax3)

plt.xticks(rotation=45)
plt.ylabel("Runs")

st.pyplot(fig3)

st.markdown("*Top batsmen consistently score the highest runs across seasons.*")

# ---- TOP BOWLERS ----
st.markdown("---")
st.subheader("Top Bowlers")

wickets = deliveries[deliveries["dismissal_kind"].notna()]

top_bowlers = wickets.groupby("bowler")["dismissal_kind"].count().sort_values(ascending=False).head(10)

fig4, ax4 = plt.subplots()
top_bowlers.plot(kind="bar", color="#C77DFF", ax=ax4)

plt.xticks(rotation=45)
plt.ylabel("Wickets")

st.pyplot(fig4)

st.markdown("*A few bowlers dominate wicket-taking performance.*")

# ---- MATCH PHASE ANALYSIS ----
st.markdown("---")
st.subheader("Match Phase Analysis")

def get_phase(over):
    if over <= 6:
        return "Powerplay"
    elif over <= 15:
        return "Middle Overs"
    else:
        return "Death Overs"

deliveries["phase"] = deliveries["over"].apply(get_phase)

phase_runs = deliveries.groupby("phase")["batsman_runs"].sum()

fig5, ax5 = plt.subplots()
phase_runs.plot(
    kind="bar",
    color=["#FF4D8D", "#C77DFF", "#9D4EDD"],
    ax=ax5
)

plt.ylabel("Total Runs")
plt.xticks(rotation=0)

st.pyplot(fig5)

st.markdown("*More runs are typically scored in death overs due to aggressive batting.*")

# ---- FOOTER ----
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #C77DFF;'>IPL Analytics Dashboard • Created by Vidya Verma</p>",
    unsafe_allow_html=True
)