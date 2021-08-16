from datetime import datetime
import json
import pathlib
from typing import Any, Dict, List

from humps import camelize
from pydantic import BaseModel


def to_camel(text: str) -> str:
    return camelize(text)


class TeamsSchema(BaseModel):
    home_name: str
    away_name: str

    class Config:
        alias_generator = to_camel


class ResultSchema(BaseModel):
    team_home_goals: int
    team_away_goals: int

    class Config:
        alias_generator = to_camel


class RefereeSchema(BaseModel):
    referee_type: str
    referee_name: str

    class Config:
        alias_generator = to_camel


class MatchDetailsSchema(BaseModel):
    match_id: int
    league_name: str
    season_name: str
    teams: TeamsSchema
    venue_name: str
    date: datetime
    result: ResultSchema
    referees: List[RefereeSchema]

    class Config:
        alias_generator = to_camel


def load_data(file_name: str) -> Dict[str, Any]:
    with (pathlib.Path(__file__).parent / file_name).open() as json_file:
        return json.load(json_file)


if __name__ == "__main__":
    match_request = load_data("match_request.json")
    match_details = MatchDetailsSchema(**match_request)
    print(repr(match_details))
