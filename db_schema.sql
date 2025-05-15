-- Simplified DB Schema for LDM Dashboard
CREATE TABLE IF NOT EXISTS engagements (
    id SERIAL PRIMARY KEY,
    status VARCHAR(32), -- green, yellow, red
    client_engagement VARCHAR(255),
    date DATE,
    major_urgent_callouts TEXT,
    slack_link TEXT
);
