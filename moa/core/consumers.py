# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class NoteConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.conversation_seed_name = self.scope["url_route"]["kwargs"]["seed_note_id"]
		self.conversation_group_name = f"conversation_{self.conversation_seed_name}"

		# Join room group
		await self.channel_layer.group_add(self.conversation_group_name, self.channel_name)

		await self.accept()

	async def disconnect(self, close_code):
		# Leave room group
		await self.channel_layer.group_discard(self.conversation_group_name, self.channel_name)

	# Receive message from WebSocket
	async def receive(self, text_data):
		note_data_json = json.loads(text_data)
		note = note_data_json["note"]
		user = note_data_json["user"]
		note_id = note_data_json["noteID"]
		created_at = note_data_json["createdAt"]
		parent_id = note_data_json["parentID"]
		level = int(note_data_json["parentLevel"]) + 1

		# Send message to room group
		await self.channel_layer.group_send(
			self.conversation_group_name, {"type": "conversation.note", "note": note, "user": user, 
								  "createdAt": created_at, "noteID": note_id, "parentID": parent_id, "level": level}
		)

	# Receive message from room group
	async def conversation_note(self, event):
		note = event["note"]
		user = event["user"]
		note_id = event["noteID"]
		created_at = event["createdAt"]
		parent_id = event["parentID"]
		level = event["level"]
		# Send message to WebSocket
		await self.send(text_data=json.dumps({"note": note, "user": user, 
										"createdAt": created_at, "noteID": note_id, "parentID": parent_id, "level": level}))


class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		# re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
		self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
		self.room_group_name = f"chat_{self.room_name}"

		# Join room group
		await self.channel_layer.group_add(self.room_group_name, self.channel_name)

		await self.accept()

	async def disconnect(self, close_code):
		# Leave room group
		await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

	# Receive message from WebSocket
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]

		# Send message to room group
		await self.channel_layer.group_send(
			self.room_group_name, {"type": "chat.message", "message": message}
		)

	# Receive message from room group
	async def chat_message(self, event):
		message = event["message"]

		# Send message to WebSocket
		await self.send(text_data=json.dumps({"message": message}))
