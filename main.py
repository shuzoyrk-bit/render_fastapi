from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>ようこそ！</h1>
            <p>課題のページです</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/food")
async def favorite_food(food):
    return {
        "message": f"{food}を教えてくれてありがとう！"
    }
