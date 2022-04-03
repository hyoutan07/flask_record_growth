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

  // クリア処理
  function deletelocalstrage() {
    localStorage.removeItem('tiltle-textarea');
    document.getElementById('tiltle-textarea').value = '';
    for (let i = 1; i < 10; i++) {
      for (let j = 1; j < 10; j++) {
        var x = "column" + String(i) + "-" + String(j) + "-textarea";
        localStorage.removeItem(x);
        document.getElementById(x).value = '';
      } 
    }
  }

  function send_test() {
    console.log("クリック！")

    const send_data = {
      message: "JSから送ったよ！",
      column_11: document.getElementById("column1-1-textarea").value,
      column_12: document.getElementById("column1-2-textarea").value,
      column_13: document.getElementById("column1-3-textarea").value,
      column_14: document.getElementById("column1-4-textarea").value,
      column_15: document.getElementById("column1-5-textarea").value,
      column_16: document.getElementById("column1-6-textarea").value,
      column_17: document.getElementById("column1-7-textarea").value,
      column_18: document.getElementById("column1-8-textarea").value,
      column_19: document.getElementById("column1-9-textarea").value, 

      column_21: document.getElementById("column2-1-textarea").value,
      column_22: document.getElementById("column2-2-textarea").value,
      column_23: document.getElementById("column2-3-textarea").value,
      column_24: document.getElementById("column2-4-textarea").value,
      column_25: document.getElementById("column2-5-textarea").value,
      column_26: document.getElementById("column2-6-textarea").value,
      column_27: document.getElementById("column2-7-textarea").value,
      column_28: document.getElementById("column2-8-textarea").value,
      column_29: document.getElementById("column2-9-textarea").value,  
    
      column_31: document.getElementById("column3-1-textarea").value,
      column_32: document.getElementById("column3-2-textarea").value,
      column_33: document.getElementById("column3-3-textarea").value,
      column_34: document.getElementById("column3-4-textarea").value,
      column_35: document.getElementById("column3-5-textarea").value,
      column_36: document.getElementById("column3-6-textarea").value,
      column_37: document.getElementById("column3-7-textarea").value,
      column_38: document.getElementById("column3-8-textarea").value,
      column_39: document.getElementById("column3-9-textarea").value,

      column_41: document.getElementById("column4-1-textarea").value,
      column_42: document.getElementById("column4-2-textarea").value,
      column_43: document.getElementById("column4-3-textarea").value,
      column_44: document.getElementById("column4-4-textarea").value,
      column_45: document.getElementById("column4-5-textarea").value,
      column_46: document.getElementById("column4-6-textarea").value,
      column_47: document.getElementById("column4-7-textarea").value,
      column_48: document.getElementById("column4-8-textarea").value,
      column_49: document.getElementById("column4-9-textarea").value,
  
      column_51: document.getElementById("column1-5-textarea").value,
      column_52: document.getElementById("column2-5-textarea").value,
      column_53: document.getElementById("column3-5-textarea").value,
      column_54: document.getElementById("column4-5-textarea").value,
      column_55: document.getElementById("column5-5-textarea").value,
      column_56: document.getElementById("column6-5-textarea").value,
      column_57: document.getElementById("column7-5-textarea").value,
      column_58: document.getElementById("column8-5-textarea").value,
      column_59: document.getElementById("column9-5-textarea").value,

      column_61: document.getElementById("column6-1-textarea").value,
      column_62: document.getElementById("column6-2-textarea").value,
      column_63: document.getElementById("column6-3-textarea").value,
      column_64: document.getElementById("column6-4-textarea").value,
      column_65: document.getElementById("column6-5-textarea").value,
      column_66: document.getElementById("column6-6-textarea").value,
      column_67: document.getElementById("column6-7-textarea").value,
      column_68: document.getElementById("column6-8-textarea").value,
      column_69: document.getElementById("column6-9-textarea").value,

      column_71: document.getElementById("column7-1-textarea").value,
      column_72: document.getElementById("column7-2-textarea").value,
      column_73: document.getElementById("column7-3-textarea").value,
      column_74: document.getElementById("column7-4-textarea").value,
      column_75: document.getElementById("column7-5-textarea").value,
      column_76: document.getElementById("column7-6-textarea").value,
      column_77: document.getElementById("column7-7-textarea").value,
      column_78: document.getElementById("column7-8-textarea").value,
      column_79: document.getElementById("column7-9-textarea").value,

      column_81: document.getElementById("column8-1-textarea").value,
      column_82: document.getElementById("column8-2-textarea").value,
      column_83: document.getElementById("column8-3-textarea").value,
      column_84: document.getElementById("column8-4-textarea").value,
      column_85: document.getElementById("column8-5-textarea").value,
      column_86: document.getElementById("column8-6-textarea").value,
      column_87: document.getElementById("column8-7-textarea").value,
      column_88: document.getElementById("column8-8-textarea").value,
      column_89: document.getElementById("column8-9-textarea").value,

      column_91: document.getElementById("column9-1-textarea").value,
      column_92: document.getElementById("column9-2-textarea").value,
      column_93: document.getElementById("column9-3-textarea").value,
      column_94: document.getElementById("column9-4-textarea").value,
      column_95: document.getElementById("column9-5-textarea").value,
      column_96: document.getElementById("column9-6-textarea").value,
      column_97: document.getElementById("column9-7-textarea").value,
      column_98: document.getElementById("column9-8-textarea").value,
      column_99: document.getElementById("column9-9-textarea").value,
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