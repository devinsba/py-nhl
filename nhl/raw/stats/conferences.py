from dataclasses import dataclass
from typing import List

import requests
from dataclasses_json import dataclass_json, LetterCase

from .common import BaseResponse, SERVER_ADDRESS

PATH = "/api/v1/conferences"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Conference:
    id: int
    name: str
    link: str
    abbreviation: str
    short_name: str
    active: bool


@dataclass_json
@dataclass(frozen=True)
class ConferencesResponse(BaseResponse):
    conferences: List[Conference]


def get(conference_id=None):
    url = SERVER_ADDRESS + PATH
    if conference_id is not None:
        url = url + "/{}".format(conference_id)
    return ConferencesResponse.from_json(requests.get(url).text)
