# LDM Dashboard

A simple but also pretty rad and humble dashboard for tracking and visualizing standardized workstream updates across company engagements. Built with Streamlit and PostgreSQL, this app allows you to:

- View the current and historical status of all client engagements (Green/Yellow/Red)
- Drill down into individual engagement trends
- Visualize engagement status breakdowns with a sunburst chart
- Store and retrieve updates using a PostgreSQL database (run via Docker)

## Features
- **Overall Status Trends:** See all engagement statuses over time and a sunburst chart breakdown.
- **Engagement Trends:** Filter and visualize the status history for a specific engagement.
- **All Engagement Updates:** Review all updates, callouts, and Slack links for each engagement.

---

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/) (for running PostgreSQL)
- [Python 3.8+](https://www.python.org/)
- Recommended: Use a Python virtual environment (`python3 -m venv venv`)

### Install Python dependencies
```sh
pip install -r requirements.txt
```

### Database & App Setup (with Makefile)
All commands are run from the project root.

#### Start the database (in Docker):
```sh
make db-up
```

#### Wait for DB, initialize schema, and load test data:
```sh
make db-init
make db-testdata
```

#### Or run everything (including the Streamlit app):
```sh
make all
```

#### Stop the database:
```sh
make db-down
```

#### Run the Streamlit dashboard (if DB is already running):
```sh
make streamlit-up
```

---

## File Overview
- `streamlit_app.py` — Main dashboard app
- `db_module.py` — Database connection and data extraction
- `db_schema.sql` — Database schema
- `db_test_data.sql` — Test data for demo/trends
- `Makefile` — Easy commands for setup and running

---

## Customization
- To add real data, update the database or modify the test data SQL file.
- To change engagement fields or visualizations, edit `streamlit_app.py`.

---

## Example Visualizations
- **Sunburst Chart:** Shows which engagements are green/yellow/red (latest status)
- **Status Trend Dots:** See how each engagement’s status changes over time

---

## Contact
For questions or improvements, open an issue or pull request on this repo.
