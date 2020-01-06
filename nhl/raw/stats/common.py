from dataclasses import dataclass

SERVER_ADDRESS = "https://statsapi.web.nhl.com"


@dataclass(frozen=True)
class BaseResponse:
    copyright: str
