from enum import Enum
from pydantic import BaseModel

class BrazilianStates(str, Enum):
    sp = 'SP',
    rj = 'RJ',
    mg = 'MG'


class NF(BaseModel):
    descricao: str
    valor: float

    def from_response(self, response):
        return self