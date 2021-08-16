from datetime import datetime
import json
import pathlib
from typing import Any, Dict, List

from pydantic import BaseModel


class TeamsSchema(BaseModel):
    homeName: str
    awayName: str


class ResultSchema(BaseModel):
    teamHomeGoals: int
    teamAwayGoals: int


class RefereeSchema(BaseModel):
    refereeType: str
    refereeName: str


class MatchDetailsSchema(BaseModel):
    matchId: int
    leagueName: str
    seasonName: str
    teams: TeamsSchema
    venueName: str
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
