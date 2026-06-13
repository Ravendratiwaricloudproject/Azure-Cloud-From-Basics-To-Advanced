import logging
import os
import azure.functions as func
from azure.communication.email import EmailClient

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="event")
def EventGridBlobTrigger(event: func.EventGridEvent):

    data = event.get_json()
    blob_url = data.get("url")
    blob_name = blob_url.split("/")[-1] if blob_url else "Unknown"

    conn_str = os.getenv("ACS_CONNECTION_STRING")
    sender = os.getenv("ACS_SENDER_ADDRESS")
    recipient = os.getenv("TO_EMAIL")

    if not all([conn_str, sender, recipient, blob_url]):
        logging.error("Missing required configuration or blob URL")
        return

    try:
        client = EmailClient.from_connection_string(conn_str)

        message = {
            "senderAddress": sender,
            "recipients": {"to": [{"address": recipient}]},
            "content": {
                "subject": "Blob Created Notification",
                "plainText": f"New blob created:\n\nName: {blob_name}\nURL: {blob_url}"
            }
        }

        client.begin_send(message).result()
        logging.info("Email sent successfully")

    except Exception as e:
        logging.error(f"Email send failed: {e}")