let Data = { Title: "サンプルタイトル", URL: "http://www.sample.com" };// あとで入れる

// prependChildを定義
Element.prototype.prependChild = function(el){
  this.insertBefore(el, this.firstChild)
}

var bodyElement = document.querySelector('body');
var heavyTire = document.createElement('div');

// ここからコンテンツを作る

// heavyTire.className = 'heavy-tire';
heavyTire.textContent = '追加テキスト';

// ここまで

bodyElement.prependChild(heavyTire);