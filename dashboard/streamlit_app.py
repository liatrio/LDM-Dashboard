import streamlit as st
from db_module import fetch_engagements

st.title('LDM Workstream Dashboard')

engagements = fetch_engagements()

import pandas as pd

if not engagements:
    st.warning('No engagement data found.')
else:
    # Convert to DataFrame for easier trend plotting
    df = pd.DataFrame(engagements, columns=["status", "client_engagement", "date", "major_urgent_callouts", "slack_link"])
    df["date"] = pd.to_datetime(df["date"])

    # Sidebar page navigation
    page = st.sidebar.radio(
        "Navigate",
        ("Overall Status Trends", "Engagement Trends")
    )
    # Engagement filter only for Engagement Trends page
    if page == "Engagement Trends":
        engagement_options = ["All Engagements"] + list(df["client_engagement"].unique())
        selected_engagement = st.selectbox("Filter by Engagement", engagement_options)
    else:
        selected_engagement = "All Engagements"

    # Map status to numeric for plotting
    status_map = {"green": 2, "yellow": 1, "red": 0}
    status_color_map = {
        "green": "#21ba45",
        "yellow": "#fbbd08",
        "red": "#db2828"
    }
    df["status_numeric"] = df["status"].map(status_map)
    df["status_color"] = df["status"].map(status_color_map)

    import altair as alt

    if page == "Overall Status Trends":
        st.header("Overall Status Trends (All Engagements)")

        # Sunburst chart for status breakdown
        import plotly.express as px
        # For each engagement, use the latest status by date
        latest_status_df = df.sort_values('date').groupby('client_engagement').tail(1)
        sunburst_fig = px.sunburst(
            latest_status_df,
            path=['status', 'client_engagement'],
            values=None,
            color='status',
            color_discrete_map=status_color_map,
            title="Engagements by Status"
        )
        st.plotly_chart(sunburst_fig, use_container_width=True)

        overall_points = alt.Chart(df).mark_circle(size=120).encode(
            x=alt.X('date:T', title='Date'),
            y=alt.Y('status_numeric:Q', title='Status (Green=2, Yellow=1, Red=0)'),
            color=alt.Color('status:N', scale=alt.Scale(domain=list(status_color_map.keys()), range=list(status_color_map.values())), legend=None),
            tooltip=['date', 'status', 'client_engagement']
        )
        st.altair_chart(overall_points, use_container_width=True)
        st.caption("Green = 2, Yellow = 1, Red = 0")

    elif page == "Engagement Trends":
        st.header("Status Trend for Selected Engagement")
        if selected_engagement == "All Engagements":
            st.info("Please select a specific engagement to view its trend.")
        else:
            trend_df = df[df["client_engagement"] == selected_engagement].sort_values("date")
            points = alt.Chart(trend_df).mark_circle(size=120).encode(
                x=alt.X('date:T', title='Date'),
                y=alt.Y('status_numeric:Q', title='Status (Green=2, Yellow=1, Red=0)'),
                color=alt.Color('status:N', scale=alt.Scale(domain=list(status_color_map.keys()), range=list(status_color_map.values())), legend=None),
                tooltip=['date', 'status']
            )
            st.altair_chart(points, use_container_width=True)
            st.caption("Green = 2, Yellow = 1, Red = 0")

    # Show all records below, filtered if an engagement is selected
    st.subheader("All Engagement Updates")
    if selected_engagement == "All Engagements":
        filtered_df = df
    else:
        filtered_df = df[df["client_engagement"] == selected_engagement]
    for idx, row in filtered_df.iterrows():
        st.markdown(f"### Status: {row['status'].title()} | {row['client_engagement']} | {row['date'].date()}")
        st.markdown(f"**Major/Urgent Callouts:**<br>{row['major_urgent_callouts']}", unsafe_allow_html=True)
        if row['slack_link']:
            st.markdown(f"[View Slack Thread]({row['slack_link']})")
        st.markdown("---")
