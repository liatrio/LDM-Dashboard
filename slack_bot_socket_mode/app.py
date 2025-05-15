import os
from dotenv import load_dotenv
from slack_sdk.web import WebClient
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest

# Load environment variables from .env file
load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN") # Make sure this is in your .env

# Initialize SocketModeClient with an app-level token + WebClient
client = SocketModeClient(
    # This app-level token will be used only for establishing a connection
    app_token=SLACK_APP_TOKEN,
    # You will be using this WebClient for performing Web API calls in listeners
    web_client=WebClient(token=SLACK_BOT_TOKEN)
)

def process(client: SocketModeClient, req: SocketModeRequest):
    if req.type == "events_api":
        # Acknowledge the request anyway
        response = SocketModeClient.response(req.envelope_id)
        client.send_socket_mode_response(response)

        # Add logic here to handle events subscription
        # (Events API: https://api.slack.com/events-api)
        if req.payload["event"]["type"] == "message" \
            and req.payload["event"].get("subtype") is None \
            and req.payload["event"]["user"] != client.web_client.auth_test()["user_id"]:
            
            channel_id = req.payload["event"]["channel"]
            message_text = req.payload["event"]["text"]
            print(f"Received message: '{message_text}' in channel {channel_id}")
            
            # Example: Echo the message back
            # try:
            #     client.web_client.chat_postMessage(
            #         channel=channel_id,
            #         text=f"You said: {message_text}"
            #     )
            # except Exception as e:
            #     print(f"Error posting message: {e}")

    if req.type == "interactive":
        # Acknowledge the request anyway
        response = SocketModeClient.response(req.envelope_id)
        client.send_socket_mode_response(response)
        # Add logic here to handle interactive events
        print(f"Received interactive event: {req.payload}")
        return

    if req.type == "slash_commands":
        # Acknowledge the request anyway
        response = SocketModeClient.response(req.envelope_id)
        client.send_socket_mode_response(response)
        # Add logic here to handle slash commands
        # (Slash Commands: https://api.slack.com/interactivity/slash-commands)
        print(f"Received slash command: {req.payload}")
        return

# Add a new listener to receive messages from Slack
# You can add more listeners like this
client.socket_mode_request_listeners.append(process)

if __name__ == "__main__":
    if not SLACK_BOT_TOKEN or not SLACK_APP_TOKEN:
        print("Error: SLACK_BOT_TOKEN or SLACK_APP_TOKEN not found. Please check your .env file.")
    else:
        print("Starting Slack bot in Socket Mode...")
        # Establish a WebSocket connection to the Socket Mode servers
        client.connect()
        # Just not to stop this process
        from threading import Event
        Event().wait()
