from fastapi import FastAPI, Request

app = FastAPI()


@app.get('/')
async def index(request: Request):
    """docs"""
    return {
        'message': 'index page',
        'base_url': request.base_url
    }
