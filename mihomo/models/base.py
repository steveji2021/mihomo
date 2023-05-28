from pydantic import BaseModel, Field

from .character import Character
from .player import Player, PlayerSpaceInfo


class StarrailInfoParsed(BaseModel):
    """
    Mihomo parsed data

    Attributes:
        - player (`Player`): The player's basic info.
        - player_details (`PlayerSpaceInfo`): The player's details.
        - characters (list[`Character`]): The list of characters.
    """

    player: Player
    """Player's basic info"""
    player_details: PlayerSpaceInfo = Field(..., alias="PlayerSpaceInfo")
    """Player's details"""
    characters: list[Character]
    """The list of characters"""
