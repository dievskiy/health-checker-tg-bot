from core import sender, token_file_handler, config
import requests
from typing import List, Optional
import datetime
import json

now_time = str(datetime.datetime.now())


def check():
    try:
        response = _check()
        if response:
            sender.send_alert(response)
        else:
            sender.send_alert(f'OK - {now_time}')
    except ValueError as e:
        sender.send_alert(f"Exception: \n {e}")


def _check() -> Optional[str]:
    """
    Main health check logic. Sends a request to an api and if problems occur calls send method
    """
    tokens = token_file_handler.read_tokens_from_file()
    if not tokens:
        return "Tokens file is empty"
    refresh_response = requests.post(config.Config.refresh_url,
                                     data=json.dumps({"refresh_token": tokens[1].strip(), "user_id": config.Config.user_id}),
                                     headers={'Content-type': 'application/json'}).json()
    if "access_token" not in refresh_response or "refresh_token" not in refresh_response:
        return "Invalid response while refreshing tokens: \n" + str(refresh_response)
    else:
        tokens = [refresh_response["access_token"], refresh_response["refresh_token"]]
        token_file_handler.write_tokens_to_file(tokens)
        access_token = tokens[0]
        headers = {'Authorization': f"Bearer {access_token}"}
        message_response = requests.post(config.Config.message_url,
                                         data=json.dumps(
                                             {"channel_id": "188", "content": now_time}),
                                         headers=headers)
        if message_response.status_code != 201:
            return f"Message not created (!=201): \n {message_response.text}, {message_response.status_code}"
