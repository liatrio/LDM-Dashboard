-- Expanded test data for LDM Dashboard
INSERT INTO engagements (status, client_engagement, date, major_urgent_callouts, slack_link) VALUES
('yellow', 'First American - Lower AWS Spend', '2025-05-07', 'Engagement in yellow status because of risks around AWS cost savings targets. Stakeholders want to move to Green or Red next week. All other work is on schedule and meeting expectations.', 'https://slack.com/example-thread-link'),
('green', 'First American - Lower AWS Spend', '2025-05-14', 'All AWS cost savings targets met. Engagement moved to green status.', 'https://slack.com/example-thread-link2'),
('red', 'First American - Lower AWS Spend', '2025-04-30', 'Major delays in AWS account migration. Immediate action required.', 'https://slack.com/example-thread-link3'),
('yellow', 'Acme Corp - Cloud Migration', '2025-05-01', 'Some blockers with cloud vendor. Monitoring closely.', 'https://slack.com/example-thread-link4'),
('green', 'Acme Corp - Cloud Migration', '2025-05-10', 'All blockers resolved. Project on track.', 'https://slack.com/example-thread-link5'),
('yellow', 'Acme Corp - Cloud Migration', '2025-05-15', 'Minor issues resurfaced, but manageable.', 'https://slack.com/example-thread-link6'),
('red', 'Beta Inc - Security Audit', '2025-05-02', 'Critical vulnerabilities found. Audit failed.', 'https://slack.com/example-thread-link7'),
('yellow', 'Beta Inc - Security Audit', '2025-05-09', 'Most vulnerabilities patched. Awaiting final review.', 'https://slack.com/example-thread-link8'),
('green', 'Beta Inc - Security Audit', '2025-05-16', 'Audit passed. All issues resolved.', 'https://slack.com/example-thread-link9'),
('green', 'Gamma LLC - Data Lake', '2025-05-05', 'Initial launch successful. No issues reported.', 'https://slack.com/example-thread-link10'),
('yellow', 'Gamma LLC - Data Lake', '2025-05-12', 'Performance issues detected. Monitoring and tuning ongoing.', 'https://slack.com/example-thread-link11'),
('red', 'Gamma LLC - Data Lake', '2025-05-19', 'System outage. Root cause analysis in progress.', 'https://slack.com/example-thread-link12');
