from typing import Any, Literal, Union

from pydantic import BaseModel, Field


class RefactRequest(BaseModel):
    prompt: str = Field(..., description="User initial input")


# --- Action Models for ActRequest ---
class MathActionsDivide(BaseModel):
    action_method_name: Literal["divide"] = Field(default="divide")
    a: float
    b: float


class MathActionsMultiply(BaseModel):
    action_method_name: Literal["multiply"] = Field(default="multiply")
    a: float
    b: float


class MathActionsPower(BaseModel):
    action_method_name: Literal["power"] = Field(default="power")
    a: float
    b: float


class MathActionsSubtract(BaseModel):
    action_method_name: Literal["subtract"] = Field(default="subtract")
    a: float
    b: float


class MathActionsSum(BaseModel):
    action_method_name: Literal["sum"] = Field(default="sum")
    a: float
    b: float


class SearchActionsLookup(BaseModel):
    action_method_name: Literal["lookup"] = Field(default="lookup")
    entity: str
    string: str


class SearchActionsSearch(BaseModel):
    action_method_name: Literal["search"] = Field(default="search")
    entity: str


# Discriminated union for action
ActionType = Union[
    MathActionsDivide,
    MathActionsMultiply,
    MathActionsPower,
    MathActionsSubtract,
    MathActionsSum,
    SearchActionsLookup,
    SearchActionsSearch,
]


class ActRequest(BaseModel):
    """Request schema for /act endpoint."""

    action: ActionType = Field(
        ..., discriminator="action_method_name", description="Action to be executed"
    )


class ActResponse(BaseModel):
    """Response schema for /act endpoint."""

    result: Any = Field(..., description="Action result")


class ReasonRequest(RefactRequest):
    """Request schema for /reason endpoint."""

    pass


class ReasonResponse(BaseModel):
    """
    Response schema for /reason endpoint.
    """

    text: str = Field(..., description="Reasoning text")
