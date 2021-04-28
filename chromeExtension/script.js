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
  const txtBox = document.querySelector("input");
  document.querySelector("button.ttl").addEventListener("click", () => {
    // クリックされたときにテキストボックスに出力
    txtBox.value = Data.Title;
  });
  document.querySelector("button.url").addEventListener("click", () => {
    txtBox.value = Data.URL;
  });
  document.querySelector("button.bmark").addEventListener("click", () => {
    txtBox.value = "AAAAAAAA";
  });
});
