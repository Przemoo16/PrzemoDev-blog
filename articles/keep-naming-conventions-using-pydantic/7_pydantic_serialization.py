from datetime import datetime, timezone
from typing import List

from humps import camelize
from pydantic import BaseModel


def to_camel(text: str) -> str:
    return camelize(text)


class CamelCaseModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class TeamsSchema(CamelCaseModel):
    home_name: str
    away_name: str


class ResultSchema(CamelCaseModel):
    team_home_goals: int
    team_away_goals: int


class RefereeSchema(CamelCaseModel):
    referee_type: str
    referee_name: str


class MatchDetailsSchema(CamelCaseModel):
    match_id: int
    league_name: str
    season_name: str
    teams: TeamsSchema
    venue_name: str
    date: datetime
    result: ResultSchema
    referees: List[RefereeSchema]


if __name__ == "__main__":
    match_response = {
        "match_id": 11955,
        "league_name": "UEFA Champions League",
        "season_name": "UEFA Champions League - 2019/2020",
        "teams": {
            "home_name": "Paris Saint-Germain F.C.",
            "away_name": "FC Bayern Munich",
        },
        "venue_name": "Estadio da Luz",
        "date": datetime(2020, 8, 23, 19, 0, tzinfo=timezone.utc),
        "result": {
            "team_home_goals": 0,
            "team_away_goals": 1,
        },
        "referees": [
            {
                "referee_type": "main",
                "referee_name": "Daniele Orsato",
            },
            {
                "referee_type": "assistant",
                "referee_name": "Lorenzo Manganelli",
            },
            {
                "referee_type": "assistant",
                "referee_name": "Alessandro Giallatini",
            },
            {
                "referee_type": "assistant",
                "referee_name": "Ovidiu Hategan",
            },
        ],
    }
    match_details = MatchDetailsSchema(**match_response)
    print(match_details.json(by_alias=True))
