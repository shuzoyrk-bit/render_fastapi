from fastapi.responses import HTMLResponse

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>私のホームページ</title>
        </head>
        <body>
            <h1>こんにちは！</h1>
            <p>FastAPIで作ったホームページです。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
