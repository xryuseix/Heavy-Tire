// ポップアップ用スクリプト
let Data = { Title: "", URL: "" }; // とりま格納する変数

chrome.tabs.getSelected((tab) => {
  // 現在のタブを取得
  Data.Title = tab.title; // tabに現在のタブが格納されている（？）。
  Data.URL = tab.url; // tab.titleには現在開いているタブのページタイトルが、tab.urlにはURLが格納されている。
  console.log(`Title: ${Data.Title}`); // 出力は、「ポップアップを検証」で見れる。
  console.log(`URL: ${Data.URL}`);
});

// 設置を保存
function save_options() {
  var isSafeDisplay = document.getElementById("settings").checked;
  chrome.storage.sync.set(
    {
      "isSafeDisplay": isSafeDisplay,
    },
    function () {
      var status = document.getElementById("status");
      status.textContent = `保存されました : ${isSafeDisplay}`;
    }
  );
}

// 設置を初期化
function restore_options() {
  chrome.storage.sync.get(
    {
      "isSafeDisplay": true,
    },
    function (items) {
      document.getElementById("settings").checked = items.isSafeDisplay;
    }
  );
}
document.addEventListener("DOMContentLoaded", restore_options);
document.getElementById("save").addEventListener("click", save_options);
