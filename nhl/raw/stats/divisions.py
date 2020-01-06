from dataclasses import dataclass
from typing import List

import requests
from dataclasses_json import dataclass_json, LetterCase

from .common import BaseResponse, SERVER_ADDRESS
from .conferences import get as get_conferences

PATH = "/api/v1/divisions"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class DivisionConference:
    id: int
    name: str
    link: str

    def follow_link(self):
        return get_conferences(self.id)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Division:
    id: int
    name: str
    link: str
    abbreviation: str
    conference: DivisionConference
    active: bool


@dataclass_json
@dataclass(frozen=True)
class DivisionsResponse(BaseResponse):
    divisions: List[Division]


def get(division_id=None):
    url = SERVER_ADDRESS + PATH
    if division_id is not None:
        url = url + "/{}".format(division_id)
    return DivisionsResponse.from_json(requests.get(url).text)
