// prependChildを定義
Element.prototype.prependChild = function (el) {
  this.insertBefore(el, this.firstChild);
};

const bodyElement = document.querySelector("body");
const heavyTire = document.createElement("div");
heavyTire.className = "heavy-tire";
// TODO: heightを指定

// ここからコンテンツを作る

fetch(`https://heavy-tire.herokuapp.com/?url=${document.domain}`)
  // fetch("https://heavy-tire.herokuapp.com/?url=utchweb.gtphost.com/zimbra/exch/owa/uleth/index.html")
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
  if ("result" in jsonObj) {
    if (jsonObj.result) {
      // フィッシングサイト
      heavyTire.classList.add("phishing");
      heavyTire.style.backgroundColor = "#ffff66";
      heavyTire.textContent =
        "[Heavy-Tire] 閲覧しているページはフィッシングサイトである可能性があります。";
      heavyTire.style.textAlign = "center";
    } else {
      // 安全なサイト
      heavyTire.classList.add("safe");
      heavyTire.style.backgroundColor = "#00CC00";
      heavyTire.textContent = "[Heavy-Tire] 閲覧しているページは安全です。";
      heavyTire.style.textAlign = "center";
    }
  } else {
    // Error
    console.log("[Heavy-Tire] ERROR: failed to fatch.");
  }
}

// ここまで

bodyElement.prependChild(heavyTire);
