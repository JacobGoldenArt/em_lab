import logging
from typing import Dict, Any


class Lobby:
    def process(self, data: Dict[str, Any], **aux) -> Dict[str, Any]:
        print(f"Debug: data received in Lobby: {data}")  # Debugging line
        print(f"Debug: aux received in Lobby: {aux}")  # Debugging line

        if "input_text" not in data:
            raise ValueError("Missing input_text in data.")

        # Fetch recent turns from data if present
        recent_turns = data.get("recent_turns", [])

        # Create a 'context' string by concatenating recent turns
        context = ""
        for turn in recent_turns:
            context += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"

        # Add the current user input to the context
        context += f"User: {data['input_text']}"
        print(f"Debug: context created in Lobby: {context}")  # Debugging line

        logging.info(f"Received input text: {data['input_text']}")
        lobby_data = {**data, **aux, "context": context}

        return {"lobby_data": lobby_data}
