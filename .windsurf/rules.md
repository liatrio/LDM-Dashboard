# Project: LDM Workstream Dashboard (Streamlit Edition)

## Core Objective
This project aims to create a dashboard that scrapes data from the `#liatrio-weekly-workstream-update` channel in Slack. It will then process this data, store it, and display it in a user-friendly Streamlit application. The dashboard will group updates by workstream and visually indicate their status using LDM color codes (Red, Yellow, Green).

## Architecture Overview
The system will consist of three main services orchestrated by Docker Compose:

1.  **Redis:**
    *   Acts as an in-memory data store for workstream updates.

2.  **Slack Collector (`slack-collector`):**
    *   A Python service responsible for:
        *   (Initially) Generating dummy workstream updates and populating them into Redis for development and testing.
        *   (Eventually) Connecting to the Slack API to fetch real updates from the specified channel.
        *   Storing these updates in a structured format in Redis.

3.  **Streamlit Web Application (`streamlit-app`):**
    *   A Python application built with Streamlit.
    *   Responsible for:
        *   Connecting to Redis to fetch the workstream updates.
        *   Displaying the updates in a clear, card-based layout.
        *   Color-coding the cards (or elements within them) based on the LDM status (Green, Yellow, Red) associated with each update.
        *   Providing an intuitive user interface for viewing workstream statuses.

## Data Flow
1.  The `slack-collector` fetches (or generates) workstream updates.
2.  Updates are processed and stored as JSON strings in a Redis list.
3.  The `streamlit-app` retrieves the list of JSON strings from Redis.
4.  The Streamlit app parses these JSON strings and dynamically renders the information as styled cards for the user.

## Key Technologies
*   Python
*   Streamlit (for the web frontend)
*   Slack SDK (for Slack integration)
*   Redis (for data storage)
*   Docker & Docker Compose (for containerization and orchestration)

## Development Guidelines
*   Leverage `.windsurf/.to-do.md` for tracking project tasks.
*   Work iteratively, testing each component.
*   Ensure sensitive information (API keys, tokens) is managed via environment variables and `.env` files (added to `.gitignore`).


## Example workflow output

you should pull this from the example data
ldm_color=green
date=Date
workstream_name=Workstream Name
major_urgent_callouts=Major/Urgent Callouts



This is the example data we would pull from
Status
:large_green_circle: Green
Workstream Name
meher
Date
10/38
Major/Urgent Callouts
none
Concerns/Risks
none
"I need help with..."
none
General Update/Overview
none
Opportunities
none