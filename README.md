# LDM Dashboard

A simple but also pretty rad and humble dashboard for tracking and visualizing standardized workstream updates across company engagements. Built with Streamlit and Redis, this app allows you to:

- View the current and historical status of all client engagements (Green/Yellow/Red)
- Drill down into individual engagement trends
- Visualize engagement status breakdowns with a sunburst chart
- Store and retrieve updates using a Redis database (run via Docker)

## Features
- **Overall Status Trends:** See all engagement statuses over time and a sunburst chart breakdown.
- **Engagement Trends:** Filter and visualize the status history for a specific engagement.
- **All Engagement Updates:** Review all updates, callouts, and Slack links for each engagement.

---

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/) (for running Redis)
- [Python 3.8+](https://www.python.org/)
- Recommended: Use a Python virtual environment (`python3 -m venv venv`)

### Install Python dependencies
```sh
pip install -r requirements.txt
```

### Database & App Setup (with Makefile)
All commands are run from the project root.

#### Start the Redis database (in Docker):
```sh
make db-up
```

#### Load test data into Redis:
```sh
make db-testdata
```

#### Or run everything (including the Streamlit app):
```sh
make all
```

#### Stop the Redis database:
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
- `db_module.py` — Redis connection and data extraction
- `redis_test_data_loader.py` — Loads test data into Redis
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
