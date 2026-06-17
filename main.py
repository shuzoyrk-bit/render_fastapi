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
  <title>うちのペット「ポチ」紹介ページ</title>
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
    h1 { margin-top: 0; }
    .section-title {
      margin-top: 24px;
      font-weight: bold;
      font-size: 1.1rem;
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
    <div class="section-title">ポチにおやつをあげるには？</div>
    <p>
      ポチにおやつをあげる API を用意しています。  
      <strong>FastAPI の docs 画面</strong>から、好きなおやつの名前を入力して送信してください。
    </p>
    <p>
      例：<br>
      <code>present = "ビスケット"</code><br>
      と入力すると、ポチからお礼のメッセージが返ってきます。
    </p>
  </div>
</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f" {present}！ワン、ワワン。 ワン！ワンワンワンワン！！！キャオンクォン！クゥーンクンクンクーンキャイーンワオワオワオ！"
           }

