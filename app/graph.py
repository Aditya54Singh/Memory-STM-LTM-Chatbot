from langgraph.graph import START, StateGraph, END

from app.state import ChatState

from app.nodes.retrieve_memory import retrieve_memory_node
from app.nodes.chatbot import chatbot_node
from app.nodes.extract_memory import extract_memory_node
from app.nodes.save_memory import save_memory
from app.database.connection import store,checkpointer

from app.database.connection import (
    checkpointer,
    store
)

builder = StateGraph(ChatState)

builder.add_node(
    "retrieve_memory",
    retrieve_memory_node
)

builder.add_node(
    "chatbot",
    chatbot_node
)

builder.add_node(
    "extract_memory",
    extract_memory_node
)

builder.add_node(
    "save_memory",
    save_memory
)

builder.add_edge(
    START,
    "retrieve_memory",
)

builder.add_edge(
    "retrieve_memory",
    "chatbot",
)

builder.add_edge(
    "chatbot",
    "extract_memory",
)

builder.add_edge(
    "extract_memory",
    "save_memory",
)

builder.add_edge(
    "save_memory",
    END,
)

graph = builder.compile(
    checkpointer=checkpointer,
    store=store,
)
