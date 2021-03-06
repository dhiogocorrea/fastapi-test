from fastapi import FastAPI, Query, Response
from models import BrazilianStates, NF

import service

description = """
API para interagir com sistemas de nota fiscal.
"""

app = FastAPI(title="API NFs",
              description=description,
              version="0.1.0")

@app.post('/',
          summary='Insere uma nova nota fiscal')
def submit_nf(state: BrazilianStates, nf: NF):
    return Response(content = service.submit_nf(state.value, vars(nf)),
                    media_type='plain/text')


@app.get('/{nf_id}',
          summary='Retorna os dados de uma nota fiscal dado um ID de NF')
def get_nf(nf_id: str):
    return service.get_nf(nf_id)


@app.delete('/{nf_id}',
          summary='Deleta os dados de uma nota fiscal')
def delete_nf(nf_id: str):
    service.delete_nf(nf_id)
    return Response(status_code=204)