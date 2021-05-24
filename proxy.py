from fastapi import FastAPI, Response, Request
import requests


app = FastAPI()


@app.get('/{rails_path:path}')
def compound_place_proxy(request: Request, rails_path: str):

    query_params = str(request.query_params)

    print(f'Path: {rails_path}')
    print(f'Query params: {query_params}')

    url = f'http://localhost:4000/{rails_path}'

    if query_params != '':
        url += f'?{query_params}'

    res = requests.get(url)
    print(f'res.contents: {res.content}')
    return Response(content=res.content, media_type='application/xml')

