// ページ操作用スクリプト
let Data = { Title: "サンプルタイトル", URL: "http://www.sample.com" }; // あとで入れる

// prependChildを定義
Element.prototype.prependChild = function (el) {
  this.insertBefore(el, this.firstChild);
};

var bodyElement = document.querySelector("body");
var heavyTire = document.createElement("div");
heavyTire.className = "heavy-tire";

// ここからコンテンツを作る

fetch("https://heavy-tire.herokuapp.com/?url=twitter.com")
  .then((response) => {
    return response.json();
  })
  .then((result) => {
    putResponseData(result);
  })
  .catch((e) => {
    console.log(e);
  });

// APIから取得したデータを出力
function putResponseData(jsonObj) {
  // TODO: Errorの時の処理入れる
  if ("result" in jsonObj) {
    heavyTire.textContent = `{"result": ${jsonObj.result}}`;
  }else{
    console.log("[Heavy-Tire] ERROR: failed to fatch.")
  }
}

// ここまで

bodyElement.prependChild(heavyTire);
