from datetime import datetime
import json
import pathlib
from typing import Any, Dict, List

from pydantic import BaseModel, Field


class TeamsSchema(BaseModel):
    home_name: str = Field(..., alias="homeName")
    away_name: str = Field(..., alias="awayName")


class ResultSchema(BaseModel):
    team_home_goals: int = Field(..., alias="teamHomeGoals")
    team_away_goals: int = Field(..., alias="teamAwayGoals")


class RefereeSchema(BaseModel):
    referee_type: str = Field(..., alias="refereeType")
    referee_name: str = Field(..., alias="refereeName")


class MatchDetailsSchema(BaseModel):
    match_id: int = Field(..., alias="matchId")
    league_name: str = Field(..., alias="leagueName")
    season_name: str = Field(..., alias="seasonName")
    teams: TeamsSchema
    venue_name: str = Field(..., alias="venueName")
    date: datetime
    result: ResultSchema
    referees: List[RefereeSchema]


def load_data(file_name: str) -> Dict[str, Any]:
    with (pathlib.Path(__file__).parent / file_name).open() as json_file:
        return json.load(json_file)


if __name__ == "__main__":
    match_request = load_data("match_request.json")
    match_details = MatchDetailsSchema(**match_request)
    print(repr(match_details))
