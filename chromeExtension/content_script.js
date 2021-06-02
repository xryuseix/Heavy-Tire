// prependChildを定義
function setHeavyTireElement() {
  Element.prototype.prependChild = function (el) {
    this.insertBefore(el, this.firstChild);
  };

  const bodyElement = document.querySelector("body");
  const heavyTire = document.createElement("div");
  heavyTire.className = "heavy-tire";
  bodyElement.prependChild(heavyTire);
  // TODO: heightを指定
  return heavyTire;
}

// 設定の取得
async function getSettings() {
  const settings = new Promise(function (resolve, reject) {
    chrome.storage.sync.get(function (settings) {
      if (Object.keys(settings).length === 0) {
        settings.isSafeDisplay = true;
      }
      resolve(settings);
    });
  });
  return settings;
}

// フィシング判定結果を取得
function fetchPhisingAPI(heavyTire, settings) {
  fetch(`https://heavy-tire.herokuapp.com/?url=${document.domain}`)
    // fetch("https://heavy-tire.herokuapp.com/?url=utchweb.gtphost.com/zimbra/exch/owa/uleth/index.html")
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      putResponseData(heavyTire, settings, result);
    })
    .catch((e) => {
      console.log(e);
    });
}

// APIから取得したデータを出力
function putResponseData(heavyTire, settings, fetchObj) {
  if ("result" in fetchObj) {
    if (fetchObj.result) {
      // フィッシングサイト
      heavyTire.classList.add("phishing");
      heavyTire.style.backgroundColor = "#ffff66";
      heavyTire.style.textAlign = "center";
      heavyTire.textContent =
        "[Heavy-Tire] 閲覧しているページはフィッシングサイトである可能性があります。";
    } else if (settings.isSafeDisplay) {
      // 安全なサイト
      heavyTire.classList.add("safe");
      heavyTire.style.backgroundColor = "#00CC00";
      heavyTire.style.textAlign = "center";
      heavyTire.textContent = "[Heavy-Tire] 閲覧しているページは安全です。";
    }
  } else {
    // Error
    console.log("[Heavy-Tire] ERROR: failed to fetch.");
  }
}

async function main() {
  const heavyTire = setHeavyTireElement();
  const settings = await getSettings();
  fetchPhisingAPI(heavyTire, settings);
}

main();
