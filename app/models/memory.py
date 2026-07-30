from typing import Literal

from pydantic import BaseModel, Field


class Memory(BaseModel):
    """
    Memory extracted by the Memory Extractor LLM.
    """

    category: Literal[
        "profile",
        "preference",
        "project",
        "goal",
    ]

    memory: str

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )


class RetrievedMemory(BaseModel):
    """
    Memory returned from semantic search.
    """

    key: str

    category: str

    memory: str

    score: float


class MemoryCollection(BaseModel):

    memories: list[Memory]