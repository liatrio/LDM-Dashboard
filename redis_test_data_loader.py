import redis
import json
from datetime import datetime

# Test data (mirrored from db_test_data.sql)
test_data = [
    {
        "status": "yellow",
        "client_engagement": "First American - Lower AWS Spend",
        "date": "2025-05-07",
        "major_urgent_callouts": "Engagement in yellow status because of risks around AWS cost savings targets. Stakeholders want to move to Green or Red next week. All other work is on schedule and meeting expectations.",
        "slack_link": "https://slack.com/example-thread-link"
    },
    {
        "status": "green",
        "client_engagement": "First American - Lower AWS Spend",
        "date": "2025-05-14",
        "major_urgent_callouts": "All AWS cost savings targets met. Engagement moved to green status.",
        "slack_link": "https://slack.com/example-thread-link2"
    },
    {
        "status": "red",
        "client_engagement": "First American - Lower AWS Spend",
        "date": "2025-04-30",
        "major_urgent_callouts": "Major delays in AWS account migration. Immediate action required.",
        "slack_link": "https://slack.com/example-thread-link3"
    },
    {
        "status": "yellow",
        "client_engagement": "Acme Corp - Cloud Migration",
        "date": "2025-05-01",
        "major_urgent_callouts": "Some blockers with cloud vendor. Monitoring closely.",
        "slack_link": "https://slack.com/example-thread-link4"
    },
    {
        "status": "green",
        "client_engagement": "Acme Corp - Cloud Migration",
        "date": "2025-05-10",
        "major_urgent_callouts": "All blockers resolved. Project on track.",
        "slack_link": "https://slack.com/example-thread-link5"
    },
    {
        "status": "yellow",
        "client_engagement": "Acme Corp - Cloud Migration",
        "date": "2025-05-15",
        "major_urgent_callouts": "Minor issues resurfaced, but manageable.",
        "slack_link": "https://slack.com/example-thread-link6"
    },
    {
        "status": "red",
        "client_engagement": "Beta Inc - Security Audit",
        "date": "2025-05-02",
        "major_urgent_callouts": "Critical vulnerabilities found. Audit failed.",
        "slack_link": "https://slack.com/example-thread-link7"
    },
    {
        "status": "yellow",
        "client_engagement": "Beta Inc - Security Audit",
        "date": "2025-05-09",
        "major_urgent_callouts": "Most vulnerabilities patched. Awaiting final review.",
        "slack_link": "https://slack.com/example-thread-link8"
    },
    {
        "status": "green",
        "client_engagement": "Beta Inc - Security Audit",
        "date": "2025-05-16",
        "major_urgent_callouts": "Audit passed. All issues resolved.",
        "slack_link": "https://slack.com/example-thread-link9"
    },
    {
        "status": "green",
        "client_engagement": "Gamma LLC - Data Lake",
        "date": "2025-05-05",
        "major_urgent_callouts": "Initial launch successful. No issues reported.",
        "slack_link": "https://slack.com/example-thread-link10"
    },
    {
        "status": "yellow",
        "client_engagement": "Gamma LLC - Data Lake",
        "date": "2025-05-12",
        "major_urgent_callouts": "Performance issues detected. Monitoring and tuning ongoing.",
        "slack_link": "https://slack.com/example-thread-link11"
    },
    {
        "status": "red",
        "client_engagement": "Gamma LLC - Data Lake",
        "date": "2025-05-19",
        "major_urgent_callouts": "System outage. Root cause analysis in progress.",
        "slack_link": "https://slack.com/example-thread-link12"
    },
]

def main():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    # Clear previous data
    r.delete('engagements')
    # Store as a Redis list of JSON strings (preserves order)
    for entry in test_data:
        r.rpush('engagements', json.dumps(entry))
    print(f"Loaded {len(test_data)} engagements into Redis.")

if __name__ == "__main__":
    main()
