from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import dataclass_json, LetterCase

from .common import SERVER_ADDRESS, BaseResponse
import requests

PATH = "/api/v1/awards"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Award:
    name: str
    short_name: str
    description: str
    recipient_type: str
    image_url: str
    home_page_url: str
    link: str
    history: Optional[str] = None


@dataclass_json
@dataclass(frozen=True)
class AwardsResponse(BaseResponse):
    awards: List[Award]


def get(award_id=None):
    url = SERVER_ADDRESS + PATH
    if award_id is not None:
        url = url + "/{}".format(award_id)
    return AwardsResponse.from_json(requests.get(url).text)
