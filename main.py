from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>うちのペットにおやつをあげよう</title>
  <style>
    body {
      font-family: sans-serif;
      background: #faf7ef;
      padding: 20px;
      line-height: 1.7;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      background: #ffffff;
      padding: 20px;
      border-radius: 10px;
      border: 1px solid #ddd;
    }
    h1 {
      margin-top: 0;
    }
    .section-title {
      margin-top: 24px;
      font-weight: bold;
      font-size: 1.1rem;
    }
    input {
      padding: 6px;
      width: 70%;
      font-size: 1rem;
    }
    button {
      padding: 6px 12px;
      font-size: 1rem;
      margin-left: 4px;
    }
    .note {
      margin-top: 20px;
      font-size: 0.9rem;
      color: #555;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>🐾 うちのペット「ポチ」</h1>

    <p>
      ポチは元気いっぱいの柴犬です。  
      お散歩とおやつが大好きで、誰かがおやつをくれるとしっぽをぶんぶん振って喜びます。
    </p>

    <div class="section-title">ポチにおやつをあげてみよう</div>

    <p>
      下のフォームから、ポチにあげたいおやつの名前を送ってください。  
      送信すると、サーバからメッセージ（JSON）が返ってきます。
    </p>

    <form action="/present" method="post">
      <label for="present">おやつの名前：</label><br>
      <input id="present" name="present" placeholder="例：ビスケット、ボーロ">
      <button type="submit">おやつをあげる</button>
    </form>
  </div>
</body>
</html>

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。ポチです！ {present}ありがとう。とっても嬉しいよ。お返しにしっぽをふります。"}
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/food")
async def favorite_food(food):
    return {
        "message": f"{food}を教えてくれてありがとう！"
    }
