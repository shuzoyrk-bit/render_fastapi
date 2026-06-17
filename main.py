from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
<html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>うちのペット紹介サイト</title>
  <style>
    body { font-family: sans-serif; background: #fffaf0; padding: 20px; }
    .pet-card { background: white; padding: 20px; border-radius: 10px; width: 400px; margin: auto; }
    .pet-img { width: 100%; border-radius: 10px; }
    .section-title { margin-top: 30px; font-size: 20px; font-weight: bold; }
    #result { margin-top: 15px; padding: 10px; background: #e0ffe0; border-radius: 8px; }
  </style>
</head>
<body>

  <div class="pet-card">
    <h1>🐶 うちのペット「ポチ」</h1>
    <img src="dog.jpg" alt="pet" class="pet-img">

    <p>
      ポチは元気いっぱいの柴犬です。  
      お散歩が大好きで、特におやつをもらうととても喜びます。
    </p>

    <div class="section-title">ポチにおやつをあげよう</div>
    <p>好きなおやつの名前を入力してね。</p>

    <input id="present" placeholder="例：ビスケット" style="padding: 8px; width: 70%;">
    <button onclick="sendPresent()" style="padding: 8px 12px;">あげる</button>

    <div id="result"></div>
  </div>

  <script>
    async function sendPresent() {
      const present = document.getElementById("present").value;

      const res = await fetch("/present", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ present })
      });

      const data = await res.json();
      document.getElementById("result").textContent = data.response;
    }
  </script>
</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/food")
async def favorite_food(food):
    return {
        "message": f"{food}を教えてくれてありがとう！"
    }
