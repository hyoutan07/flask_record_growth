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

  // 外側から内側に同期
  for(let i = 1; i < 10; i++) {
    if(i != 5) {
        window.addEventListener('DOMContentLoaded', function(){
          var x = "column" + String(i) + "-" + String(5) + "-textarea";
          var text = document.getElementById(x);

          text.addEventListener("input", function() {
          var y = "column" + String(5) + "-" + String(i) + "-textarea";
          document.getElementById(y).value = document.getElementById(x).value;
        })
      })
    }
  }

  // 内側から外側に同期
  for(let i = 1; i < 10; i++) {
    if(i != 5) {
        window.addEventListener('DOMContentLoaded', function(){
          var x = "column" + String(5) + "-" + String(i) + "-textarea";
          var text = document.getElementById(x);

          text.addEventListener("input", function() {
          var y = "column" + String(i) + "-" + String(5) + "-textarea";
          document.getElementById(y).value = document.getElementById(x).value;
        })
      })
    }
  }

  // window.addEventListener("input", function synchronize() { 
  //   for(let i = 0; i < 3; i++) { 
  //     for(let j = 0; j < 3; j++) { 
  //       var x = "column" + String(3*i+1) + "-" + String(3*j+1) + "-textarea"; 
  //       var textareavalue = document.getElementById(x).value; 
  //       // var textareavalue = localStorage.getItem(x);

  //       if(textareavalue) { 
  //         var y = "column" + String(i+3) + "-" + String(j+3) + "-textarea"; 
  //         localStorage.setItem(y, textareavalue); 
  //       }
  //     }
  //   }
  // })


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


  function send_test() {
    console.log("クリック！")

    const send_data = {
      message: "JSから送ったよ！",
      mandala: document.getElementById('column1-1-textarea').value
    }
    
    // fetchで送信部分
    fetch("/create_mandala/get", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json' // おまじない
      },
      body: JSON.stringify(send_data)
    })
    .then(response => {
      return response.json();
    })
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.log("失敗しました")
    })
  }
}