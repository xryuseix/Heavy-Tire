// ポップアップ用スクリプト
let Data = { Title: "", URL: "" }; // とりま格納する変数

chrome.tabs.getSelected((tab) => {
  // 現在のタブを取得
  Data.Title = tab.title; // tabに現在のタブが格納されている（？）。
  Data.URL = tab.url; // tab.titleには現在開いているタブのページタイトルが、tab.urlにはURLが格納されている。
  console.log(`Title: ${Data.Title}`); // 出力は、「ポップアップを検証」で見れる。
  console.log(`URL: ${Data.URL}`);
});

window.addEventListener("load", () => {
  // 拡張機能アイコンがクリックされて拡張機能ポップアップページが読み込まれたとき
  const txtBox = document.getElementById("status");
  document.querySelector("button.ttl").addEventListener("click", () => {
    // クリックされたときにテキストボックスに出力
    txtBox.value = Data.Title;
  });
  document.querySelector("button.bmark").addEventListener("click", () => {
    txtBox.value = "AAAAAAAA";
  });
});

// 設置を保存
function save_options() {
  var displaySafe = document.getElementById("settings").checked;
  chrome.storage.sync.set(
    {
      displaySafe: displaySafe,
    },
    function () {
      var status = document.getElementById("status");
      status.textContent = `保存されました : ${displaySafe}`;
    }
  );
}

// 設置を初期化
function restore_options() {
  chrome.storage.sync.get(
    {
      displaySafe: true,
    },
    function (items) {
      document.getElementById("settings").checked = items.displaySafe;
    }
  );
}
document.addEventListener("DOMContentLoaded", restore_options);
document.getElementById("save").addEventListener("click", save_options);
