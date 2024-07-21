from pydantic import BaseModel
from typing import List, Optional, Union


class Authorization(BaseModel):
    enterprise_id: Optional[str]
    team_id: str
    user_id: str
    is_bot: bool
    is_enterprise_install: bool


class Element(BaseModel):
    type: str
    user_id: Optional[str] = None
    text: Optional[str] = None


class RichTextSection(BaseModel):
    type: str
    elements: List[Element]


class Block(BaseModel):
    type: str
    block_id: str
    elements: List[RichTextSection]


class Event(BaseModel):
    user: str
    type: str
    ts: str
    client_msg_id: str
    text: str
    team: str
    blocks: List[Block]
    channel: str
    event_ts: str


class SlackEvent(BaseModel):
    token: str
    team_id: str
    api_app_id: str
    event: Event
    type: str
    event_id: str
    event_time: int
    authorizations: List[Authorization]
    is_ext_shared_channel: bool
    event_context: str


class BotProfileIcons(BaseModel):
    image_36: str
    image_48: str
    image_72: str


class BotProfile(BaseModel):
    id: str
    deleted: bool
    name: str
    updated: int
    app_id: str
    icons: BotProfileIcons
    team_id: str


class BlockElement(BaseModel):
    type: str
    user_id: Optional[str] = None
    text: Optional[str] = None


class Block(BaseModel):
    type: str
    block_id: str
    elements: List[BlockElement]


class Message(BaseModel):
    user: str
    type: str
    ts: str
    client_msg_id: Optional[str] = None
    text: str
    team: str
    bot_id: Optional[str] = None
    app_id: Optional[str] = None
    bot_profile: Optional[BotProfile] = None
    blocks: List[Block]


class ResponseMetadata(BaseModel):
    next_cursor: str


class ChatHistory(BaseModel):
    ok: bool
    messages: List[Message]
    has_more: bool
    pin_count: int
    channel_actions_ts: Optional[str] = None
    channel_actions_count: int
    response_metadata: ResponseMetadata
