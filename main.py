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
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="bootstrap.css">
  <script src="bootstrap.js"></script>
  <!-- CSS only -->
  <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"> -->
  <!-- JavaScript Bundle with Popper -->
  <!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>   -->
</head>

<body>
  <!-- <nav class="navbar navbar-expand-md navbar-dark bg-dark"> -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="index.html">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="./index.html">一つ目の項目</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="index.html">二つ目の項目</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="index.html">三つ目の項目</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="index.html">四つ目の項目</a>
          </li>
        </ul>
        <button class="btn btn-outline-light" onclick="location.href='login.html'" role="button">Login</button>
        <!-- <button class="btn btn-outline-light" href="login.html" role="button">Login</button> -->
      </div>
    </div>
  </nav>

  <style>
    .main-visual-0 {
      background-color: rgba(0, 0, 0, 0.6); 
      padding-top: 3rem;
      padding-bottom: 3rem;
      /* 参考URL：
      https://developer.mozilla.org/ja/docs/Web/CSS/background-color
      https://developer.mozilla.org/ja/docs/Web/CSS/padding
      https://developer.mozilla.org/ja/docs/Learn/CSS/Building_blocks/Values_and_units */
    }
    .main-visual-1 {
      background-image: url(./img/main-visual.jpeg); 
      padding-top: 3rem;
      padding-bottom: 3rem;
      /* 参考URL：
      https://developer.mozilla.org/ja/docs/Web/CSS/background-image */
    }
    .main-visual-2 {
      background-image: url(./img/main-visual.jpeg); 
      background-size: cover;
      padding-top: 3rem;
      padding-bottom: 3rem;
      /* 参考URL：
      https://developer.mozilla.org/ja/docs/Web/CSS/background-size */
    }
    .main-visual-3 {
      background: linear-gradient(0deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(./img/main-visual.jpeg); 
      background-size: cover; 
      padding-top: 3rem;
      padding-bottom: 3rem;
      /* 参考URL：
      https://developer.mozilla.org/ja/docs/Web/CSS/linear-gradient() */
    }
    .main-visual-4 {
      background: linear-gradient(135deg, rgba(255, 0, 161, .8), rgba(4, 51, 255, .6)), url(./img/main-visual.jpeg); 
      background-size: cover; 
      padding-top: 3rem;
      padding-bottom: 3rem;
      /* 参考URL：
      https://developer.mozilla.org/ja/docs/Web/CSS/linear-gradient() */
    }
    .main-visual-5 {
      background: linear-gradient(25deg, rgba(255, 190, 44, 0.8), rgba(255, 44, 171, 0.8)), url(./img/main-visual.jpeg); 
      background-size: cover; 
      clip-path: polygon(0% 0%, 100% 0%, 100% 85%, 50% 100%, 0% 85%);
      padding-top: 3rem;
      padding-bottom: 5rem;
      /* 参考URL：
      https://developer.mozilla.org/ja/docs/Web/CSS/clip-path */
    }
  </style>
  <div class="mt-5 text-white main-visual-5">
    <div class="container">
      <h1 class="display-3">Main Visual</h1>
      <p>ページ上部に配置された大きな画像は観賞者に強い印象を与えます。この領域に配置された画像を、メインビジュアル、キービジュアル、ヒーローイメージなどと呼びます。Bootstrapではcontainerやp-5といったclass属性で確保される領域に画像を挿入することでメインビジュアルを表示できます。</p>      
      <a class="btn btn-outline-light btn-lg" href="https://www.google.com/" role="button">詳しくみる &raquo;</a>
    </div>
  </div>

  <style>
    .img-clipping-1 {
      clip-path: circle(42%);
    }
    .img-clipping-2 {
      border-radius: 0px;
      clip-path: polygon(0% 0%, 100% 0%, 100% 90%, 55% 90%, 50% 100%, 45% 90%, 0% 90%);
      /* 参考URL：
      https://developer.mozilla.org/ja/docs/Web/CSS/border-radius
      https://bennettfeely.com/clippy/ */
    }
  </style>
  <div class="container pt-4">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4">
        <div class="card mb-5 border-0 text-center">
          <img class="card-img-top img-clipping-1" src="./img/seaside.jpeg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-primary">Card Component</h5>
            <p class="card-text">Webデザインでは同種のコンテンツを複数並べて配置することが多いため、Bootstrapでは矩形領域を反復配置するためにcardというclass属性が定義されています。</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
      <div class="col-12 col-sm-6 col-md-4">
        <div class="card mb-5 border-0 text-center">
          <img class="card-img-top img-clipping-1" src="./img/food.jpeg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-primary">Card Component</h5>
            <p class="card-text">Webデザインでは同種のコンテンツを複数並べて配置することが多いため、Bootstrapでは矩形領域を反復配置するためにcardというclass属性が定義されています。</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
      <div class="col-12 col-sm-6 col-md-4">
        <div class="card mb-5 border-0 text-center">
          <img class="card-img-top img-clipping-1" src="./img/coffee.jpeg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-primary">Card Component</h5>
            <p class="card-text">Webデザインでは同種のコンテンツを複数並べて配置することが多いため、Bootstrapでは矩形領域を反復配置するためにcardというclass属性が定義されています。</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
      <!-- <div class="col-12 col-sm-6 col-md-4">
        <div class="card mb-5 border-0 text-center">
          <img class="card-img-top img-clipping-1" src="./img/room.jpeg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title text-primary">Card Component</h5>
            <p class="card-text">Webデザインでは同種のコンテンツを複数並べて配置することが多いため、Bootstrapでは矩形領域を反復配置するためにcardというclass属性が定義されています。</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div> -->
    </div>  
  </div>

  <hr class="featurette-divider">

  <footer class="container">
    <p class="p-1 float-end"><a href="#">トップに戻る</a></p>
    <p class="p-1">&copy; 2022 Footer, Inc.</p>
  </footer>

</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/food")
async def favorite_food(food):
    return {
        "message": f"{food}を教えてくれてありがとう！"
    }
