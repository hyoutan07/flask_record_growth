'use script'
{
  // ブラウザに入った時起動時にlocalstrageから入れる
  window.onload = function () {
    var textvalue = localStorage.getItem('tiltle-textarea');

    // fetchでの受け取り部分
    fetch("/create_mandala/get")
      .then(response => {
        return response.json();
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.log("失敗しました")
      })


    //値がある場合
    if (textvalue) {
      document.getElementById('tiltle-textarea').value = textvalue;
    } else {
      document.getElementById('tiltle-textarea').value = "マンダラチャートタイトル変更可能";
    }

    for (let i = 1; i < 10; i++) {
      for (let j = 1; j < 10; j++) {
        var x = "column" + String(i) + "-" + String(j) + "-textarea";
        document.getElementById(x).value = localStorage.getItem(x);
      } 
    }
  }

  // ブラウザから出た時に保存
  window.onbeforeunload = function () {
    var textareavalue = document.getElementById('tiltle-textarea').value;
    localStorage.setItem('tiltle-textarea', textareavalue);

    for (let i = 1; i < 10; i++) {
      for (let j = 1; j < 10; j++) {
        var x = "column" + String(i) + "-" + String(j) + "-textarea";
        textareavalue = document.getElementById(x).value;
        localStorage.setItem(x, textareavalue);
      } 
    }
  }

  // クリア処理
  function deletelocalstrage() {
    localStorage.removeItem('tiltle-textarea');
    document.getElementById('tiltle-textarea').value = '';
    for (let i = 1; i < 10; i++) {
      for (let j = 1; j < 10; j++) {
        var x = "column" + String(i) + "-" + String(j) + "-textarea";
        localStorage.removeItem('column1-1-textarea');
        document.getElementById('column1-1-textarea').value = '';
      } 
    }
  }
}