/**
   *起動時localstrageから値を取得
   */
   window.onload = function () {
    var textvalue = localStorage.getItem('tiltle-textarea');
    //値がある場合
    if (textvalue) {
      document.getElementById('tiltle-textarea').value = textvalue;
    } else {
      document.getElementById('tiltle-textarea').value = "マンダラチャートタイトル変更可能";
    }
    document.getElementById('column1-1-textarea').value = localStorage.getItem('column1-1-textarea');
    document.getElementById('column1-2-textarea').value = localStorage.getItem('column1-2-textarea');
    document.getElementById('column1-3-textarea').value = localStorage.getItem('column1-3-textarea');
    document.getElementById('column1-4-textarea').value = localStorage.getItem('column1-4-textarea');
    document.getElementById('column1-5-textarea').value = localStorage.getItem('column1-5-textarea');
    document.getElementById('column1-6-textarea').value = localStorage.getItem('column1-6-textarea');
    document.getElementById('column1-7-textarea').value = localStorage.getItem('column1-7-textarea');
    document.getElementById('column1-8-textarea').value = localStorage.getItem('column1-8-textarea');
    document.getElementById('column1-9-textarea').value = localStorage.getItem('column1-9-textarea');
  
    document.getElementById('column2-1-textarea').value = localStorage.getItem('column2-1-textarea');
    document.getElementById('column2-2-textarea').value = localStorage.getItem('column2-2-textarea');
    document.getElementById('column2-3-textarea').value = localStorage.getItem('column2-3-textarea');
    document.getElementById('column2-4-textarea').value = localStorage.getItem('column2-4-textarea');
    document.getElementById('column2-5-textarea').value = localStorage.getItem('column2-5-textarea');
    document.getElementById('column2-6-textarea').value = localStorage.getItem('column2-6-textarea');
    document.getElementById('column2-7-textarea').value = localStorage.getItem('column2-7-textarea');
    document.getElementById('column2-8-textarea').value = localStorage.getItem('column2-8-textarea');
    document.getElementById('column2-9-textarea').value = localStorage.getItem('column2-9-textarea');
  
    document.getElementById('column3-1-textarea').value = localStorage.getItem('column3-1-textarea');
    document.getElementById('column3-2-textarea').value = localStorage.getItem('column3-2-textarea');
    document.getElementById('column3-3-textarea').value = localStorage.getItem('column3-3-textarea');
    document.getElementById('column3-4-textarea').value = localStorage.getItem('column3-4-textarea');
    document.getElementById('column3-5-textarea').value = localStorage.getItem('column3-5-textarea');
    document.getElementById('column3-6-textarea').value = localStorage.getItem('column3-6-textarea');
    document.getElementById('column3-7-textarea').value = localStorage.getItem('column3-7-textarea');
    document.getElementById('column3-8-textarea').value = localStorage.getItem('column3-8-textarea');
    document.getElementById('column3-9-textarea').value = localStorage.getItem('column3-9-textarea');
  
    document.getElementById('column4-1-textarea').value = localStorage.getItem('column4-1-textarea');
    document.getElementById('column4-2-textarea').value = localStorage.getItem('column4-2-textarea');
    document.getElementById('column4-3-textarea').value = localStorage.getItem('column4-3-textarea');
    document.getElementById('column4-4-textarea').value = localStorage.getItem('column4-4-textarea');
    document.getElementById('column4-5-textarea').value = localStorage.getItem('column4-5-textarea');
    document.getElementById('column4-6-textarea').value = localStorage.getItem('column4-6-textarea');
    document.getElementById('column4-7-textarea').value = localStorage.getItem('column4-7-textarea');
    document.getElementById('column4-8-textarea').value = localStorage.getItem('column4-8-textarea');
    document.getElementById('column4-9-textarea').value = localStorage.getItem('column4-9-textarea');
  
    document.getElementById('column5-1-textarea').value = localStorage.getItem('column5-1-textarea');
    document.getElementById('column5-2-textarea').value = localStorage.getItem('column5-2-textarea');
    document.getElementById('column5-3-textarea').value = localStorage.getItem('column5-3-textarea');
    document.getElementById('column5-4-textarea').value = localStorage.getItem('column5-4-textarea');
    document.getElementById('column5-5-textarea').value = localStorage.getItem('column5-5-textarea');
    document.getElementById('column5-6-textarea').value = localStorage.getItem('column5-6-textarea');
    document.getElementById('column5-7-textarea').value = localStorage.getItem('column5-7-textarea');
    document.getElementById('column5-8-textarea').value = localStorage.getItem('column5-8-textarea');
    document.getElementById('column5-9-textarea').value = localStorage.getItem('column5-9-textarea');
  
    document.getElementById('column6-1-textarea').value = localStorage.getItem('column6-1-textarea');
    document.getElementById('column6-2-textarea').value = localStorage.getItem('column6-2-textarea');
    document.getElementById('column6-3-textarea').value = localStorage.getItem('column6-3-textarea');
    document.getElementById('column6-4-textarea').value = localStorage.getItem('column6-4-textarea');
    document.getElementById('column6-5-textarea').value = localStorage.getItem('column6-5-textarea');
    document.getElementById('column6-6-textarea').value = localStorage.getItem('column6-6-textarea');
    document.getElementById('column6-7-textarea').value = localStorage.getItem('column6-7-textarea');
    document.getElementById('column6-8-textarea').value = localStorage.getItem('column6-8-textarea');
    document.getElementById('column6-9-textarea').value = localStorage.getItem('column6-9-textarea');
  
    document.getElementById('column7-1-textarea').value = localStorage.getItem('column7-1-textarea');
    document.getElementById('column7-2-textarea').value = localStorage.getItem('column7-2-textarea');
    document.getElementById('column7-3-textarea').value = localStorage.getItem('column7-3-textarea');
    document.getElementById('column7-4-textarea').value = localStorage.getItem('column7-4-textarea');
    document.getElementById('column7-5-textarea').value = localStorage.getItem('column7-5-textarea');
    document.getElementById('column7-6-textarea').value = localStorage.getItem('column7-6-textarea');
    document.getElementById('column7-7-textarea').value = localStorage.getItem('column7-7-textarea');
    document.getElementById('column7-8-textarea').value = localStorage.getItem('column7-8-textarea');
    document.getElementById('column7-9-textarea').value = localStorage.getItem('column7-9-textarea');
  
    document.getElementById('column8-1-textarea').value = localStorage.getItem('column8-1-textarea');
    document.getElementById('column8-2-textarea').value = localStorage.getItem('column8-2-textarea');
    document.getElementById('column8-3-textarea').value = localStorage.getItem('column8-3-textarea');
    document.getElementById('column8-4-textarea').value = localStorage.getItem('column8-4-textarea');
    document.getElementById('column8-5-textarea').value = localStorage.getItem('column8-5-textarea');
    document.getElementById('column8-6-textarea').value = localStorage.getItem('column8-6-textarea');
    document.getElementById('column8-7-textarea').value = localStorage.getItem('column8-7-textarea');
    document.getElementById('column8-8-textarea').value = localStorage.getItem('column8-8-textarea');
    document.getElementById('column8-9-textarea').value = localStorage.getItem('column8-9-textarea');
  
    document.getElementById('column9-1-textarea').value = localStorage.getItem('column9-1-textarea');
    document.getElementById('column9-2-textarea').value = localStorage.getItem('column9-2-textarea');
    document.getElementById('column9-3-textarea').value = localStorage.getItem('column9-3-textarea');
    document.getElementById('column9-4-textarea').value = localStorage.getItem('column9-4-textarea');
    document.getElementById('column9-5-textarea').value = localStorage.getItem('column9-5-textarea');
    document.getElementById('column9-6-textarea').value = localStorage.getItem('column9-6-textarea');
    document.getElementById('column9-7-textarea').value = localStorage.getItem('column9-7-textarea');
    document.getElementById('column9-8-textarea').value = localStorage.getItem('column9-8-textarea');
    document.getElementById('column9-9-textarea').value = localStorage.getItem('column9-9-textarea');
  }
  /**
  * ブラウザフォーカスアウト時localstrage保存処理
  */
  window.onbeforeunload = function () {
    //テキストエリアから値を取得
    var textareavalue = document.getElementById('tiltle-textarea').value;
    localStorage.setItem('tiltle-textarea', textareavalue);
  
    textareavalue = document.getElementById('column1-1-textarea').value;
    localStorage.setItem('column1-1-textarea', textareavalue);
    textareavalue = document.getElementById('column1-2-textarea').value;
    localStorage.setItem('column1-2-textarea', textareavalue);
    textareavalue = document.getElementById('column1-3-textarea').value;
    localStorage.setItem('column1-3-textarea', textareavalue);
    textareavalue = document.getElementById('column1-4-textarea').value;
    localStorage.setItem('column1-4-textarea', textareavalue);
    textareavalue = document.getElementById('column1-5-textarea').value;
    localStorage.setItem('column1-5-textarea', textareavalue);
    textareavalue = document.getElementById('column1-6-textarea').value;
    localStorage.setItem('column1-6-textarea', textareavalue);
    textareavalue = document.getElementById('column1-7-textarea').value;
    localStorage.setItem('column1-7-textarea', textareavalue);
    textareavalue = document.getElementById('column1-8-textarea').value;
    localStorage.setItem('column1-8-textarea', textareavalue);
    textareavalue = document.getElementById('column1-9-textarea').value;
    localStorage.setItem('column1-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column2-1-textarea').value;
    localStorage.setItem('column2-1-textarea', textareavalue);
    textareavalue = document.getElementById('column2-2-textarea').value;
    localStorage.setItem('column2-2-textarea', textareavalue);
    textareavalue = document.getElementById('column2-3-textarea').value;
    localStorage.setItem('column2-3-textarea', textareavalue);
    textareavalue = document.getElementById('column2-4-textarea').value;
    localStorage.setItem('column2-4-textarea', textareavalue);
    textareavalue = document.getElementById('column2-5-textarea').value;
    localStorage.setItem('column2-5-textarea', textareavalue);
    textareavalue = document.getElementById('column2-6-textarea').value;
    localStorage.setItem('column2-6-textarea', textareavalue);
    textareavalue = document.getElementById('column2-7-textarea').value;
    localStorage.setItem('column2-7-textarea', textareavalue);
    textareavalue = document.getElementById('column2-8-textarea').value;
    localStorage.setItem('column2-8-textarea', textareavalue);
    textareavalue = document.getElementById('column2-9-textarea').value;
    localStorage.setItem('column2-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column3-1-textarea').value;
    localStorage.setItem('column3-1-textarea', textareavalue);
    textareavalue = document.getElementById('column3-2-textarea').value;
    localStorage.setItem('column3-2-textarea', textareavalue);
    textareavalue = document.getElementById('column3-3-textarea').value;
    localStorage.setItem('column3-3-textarea', textareavalue);
    textareavalue = document.getElementById('column3-4-textarea').value;
    localStorage.setItem('column3-4-textarea', textareavalue);
    textareavalue = document.getElementById('column3-5-textarea').value;
    localStorage.setItem('column3-5-textarea', textareavalue);
    textareavalue = document.getElementById('column3-6-textarea').value;
    localStorage.setItem('column3-6-textarea', textareavalue);
    textareavalue = document.getElementById('column3-7-textarea').value;
    localStorage.setItem('column3-7-textarea', textareavalue);
    textareavalue = document.getElementById('column3-8-textarea').value;
    localStorage.setItem('column3-8-textarea', textareavalue);
    textareavalue = document.getElementById('column3-9-textarea').value;
    localStorage.setItem('column3-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column4-1-textarea').value;
    localStorage.setItem('column4-1-textarea', textareavalue);
    textareavalue = document.getElementById('column4-2-textarea').value;
    localStorage.setItem('column4-2-textarea', textareavalue);
    textareavalue = document.getElementById('column4-3-textarea').value;
    localStorage.setItem('column4-3-textarea', textareavalue);
    textareavalue = document.getElementById('column4-4-textarea').value;
    localStorage.setItem('column4-4-textarea', textareavalue);
    textareavalue = document.getElementById('column4-5-textarea').value;
    localStorage.setItem('column4-5-textarea', textareavalue);
    textareavalue = document.getElementById('column4-6-textarea').value;
    localStorage.setItem('column4-6-textarea', textareavalue);
    textareavalue = document.getElementById('column4-7-textarea').value;
    localStorage.setItem('column4-7-textarea', textareavalue);
    textareavalue = document.getElementById('column4-8-textarea').value;
    localStorage.setItem('column4-8-textarea', textareavalue);
    textareavalue = document.getElementById('column4-9-textarea').value;
    localStorage.setItem('column4-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column5-1-textarea').value;
    localStorage.setItem('column5-1-textarea', textareavalue);
    textareavalue = document.getElementById('column5-2-textarea').value;
    localStorage.setItem('column5-2-textarea', textareavalue);
    textareavalue = document.getElementById('column5-3-textarea').value;
    localStorage.setItem('column5-3-textarea', textareavalue);
    textareavalue = document.getElementById('column5-4-textarea').value;
    localStorage.setItem('column5-4-textarea', textareavalue);
    textareavalue = document.getElementById('column5-5-textarea').value;
    localStorage.setItem('column5-5-textarea', textareavalue);
    textareavalue = document.getElementById('column5-6-textarea').value;
    localStorage.setItem('column5-6-textarea', textareavalue);
    textareavalue = document.getElementById('column5-7-textarea').value;
    localStorage.setItem('column5-7-textarea', textareavalue);
    textareavalue = document.getElementById('column5-8-textarea').value;
    localStorage.setItem('column5-8-textarea', textareavalue);
    textareavalue = document.getElementById('column5-9-textarea').value;
    localStorage.setItem('column5-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column6-1-textarea').value;
    localStorage.setItem('column6-1-textarea', textareavalue);
    textareavalue = document.getElementById('column6-2-textarea').value;
    localStorage.setItem('column6-2-textarea', textareavalue);
    textareavalue = document.getElementById('column6-3-textarea').value;
    localStorage.setItem('column6-3-textarea', textareavalue);
    textareavalue = document.getElementById('column6-4-textarea').value;
    localStorage.setItem('column6-4-textarea', textareavalue);
    textareavalue = document.getElementById('column6-5-textarea').value;
    localStorage.setItem('column6-5-textarea', textareavalue);
    textareavalue = document.getElementById('column6-6-textarea').value;
    localStorage.setItem('column6-6-textarea', textareavalue);
    textareavalue = document.getElementById('column6-7-textarea').value;
    localStorage.setItem('column6-7-textarea', textareavalue);
    textareavalue = document.getElementById('column6-8-textarea').value;
    localStorage.setItem('column6-8-textarea', textareavalue);
    textareavalue = document.getElementById('column6-9-textarea').value;
    localStorage.setItem('column6-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column7-1-textarea').value;
    localStorage.setItem('column7-1-textarea', textareavalue);
    textareavalue = document.getElementById('column7-2-textarea').value;
    localStorage.setItem('column7-2-textarea', textareavalue);
    textareavalue = document.getElementById('column7-3-textarea').value;
    localStorage.setItem('column7-3-textarea', textareavalue);
    textareavalue = document.getElementById('column7-4-textarea').value;
    localStorage.setItem('column7-4-textarea', textareavalue);
    textareavalue = document.getElementById('column7-5-textarea').value;
    localStorage.setItem('column7-5-textarea', textareavalue);
    textareavalue = document.getElementById('column7-6-textarea').value;
    localStorage.setItem('column7-6-textarea', textareavalue);
    textareavalue = document.getElementById('column7-7-textarea').value;
    localStorage.setItem('column7-7-textarea', textareavalue);
    textareavalue = document.getElementById('column7-8-textarea').value;
    localStorage.setItem('column7-8-textarea', textareavalue);
    textareavalue = document.getElementById('column7-9-textarea').value;
    localStorage.setItem('column7-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column8-1-textarea').value;
    localStorage.setItem('column8-1-textarea', textareavalue);
    textareavalue = document.getElementById('column8-2-textarea').value;
    localStorage.setItem('column8-2-textarea', textareavalue);
    textareavalue = document.getElementById('column8-3-textarea').value;
    localStorage.setItem('column8-3-textarea', textareavalue);
    textareavalue = document.getElementById('column8-4-textarea').value;
    localStorage.setItem('column8-4-textarea', textareavalue);
    textareavalue = document.getElementById('column8-5-textarea').value;
    localStorage.setItem('column8-5-textarea', textareavalue);
    textareavalue = document.getElementById('column8-6-textarea').value;
    localStorage.setItem('column8-6-textarea', textareavalue);
    textareavalue = document.getElementById('column8-7-textarea').value;
    localStorage.setItem('column8-7-textarea', textareavalue);
    textareavalue = document.getElementById('column8-8-textarea').value;
    localStorage.setItem('column8-8-textarea', textareavalue);
    textareavalue = document.getElementById('column8-9-textarea').value;
    localStorage.setItem('column8-9-textarea', textareavalue);
  
    textareavalue = document.getElementById('column9-1-textarea').value;
    localStorage.setItem('column9-1-textarea', textareavalue);
    textareavalue = document.getElementById('column9-2-textarea').value;
    localStorage.setItem('column9-2-textarea', textareavalue);
    textareavalue = document.getElementById('column9-3-textarea').value;
    localStorage.setItem('column9-3-textarea', textareavalue);
    textareavalue = document.getElementById('column9-4-textarea').value;
    localStorage.setItem('column9-4-textarea', textareavalue);
    textareavalue = document.getElementById('column9-5-textarea').value;
    localStorage.setItem('column9-5-textarea', textareavalue);
    textareavalue = document.getElementById('column9-6-textarea').value;
    localStorage.setItem('column9-6-textarea', textareavalue);
    textareavalue = document.getElementById('column9-7-textarea').value;
    localStorage.setItem('column9-7-textarea', textareavalue);
    textareavalue = document.getElementById('column9-8-textarea').value;
    localStorage.setItem('column9-8-textarea', textareavalue);
    textareavalue = document.getElementById('column9-9-textarea').value;
    localStorage.setItem('column9-9-textarea', textareavalue);
  }
  /**
  * localstrageクリア処理
  */
  function deletelocalstrage() {
    localStorage.removeItem('tiltle-textarea');
    document.getElementById('tiltle-textarea').value = '';
  
    localStorage.removeItem('column1-1-textarea');
    document.getElementById('column1-1-textarea').value = '';
    localStorage.removeItem('column1-2-textarea');
    document.getElementById('column1-2-textarea').value = '';
    localStorage.removeItem('column1-3-textarea');
    document.getElementById('column1-3-textarea').value = '';
    localStorage.removeItem('column1-4-textarea');
    document.getElementById('column1-4-textarea').value = '';
    localStorage.removeItem('column1-5-textarea');
    document.getElementById('column1-5-textarea').value = '';
    localStorage.removeItem('column1-6-textarea');
    document.getElementById('column1-6-textarea').value = '';
    localStorage.removeItem('column1-7-textarea');
    document.getElementById('column1-7-textarea').value = '';
    localStorage.removeItem('column1-8-textarea');
    document.getElementById('column1-8-textarea').value = '';
    localStorage.removeItem('column1-9-textarea');
    document.getElementById('column1-9-textarea').value = '';
  
    localStorage.removeItem('column2-1-textarea');
    document.getElementById('column2-1-textarea').value = '';
    localStorage.removeItem('column2-2-textarea');
    document.getElementById('column2-2-textarea').value = '';
    localStorage.removeItem('column2-3-textarea');
    document.getElementById('column2-3-textarea').value = '';
    localStorage.removeItem('column2-4-textarea');
    document.getElementById('column2-4-textarea').value = '';
    localStorage.removeItem('column2-5-textarea');
    document.getElementById('column2-5-textarea').value = '';
    localStorage.removeItem('column2-6-textarea');
    document.getElementById('column2-6-textarea').value = '';
    localStorage.removeItem('column2-7-textarea');
    document.getElementById('column2-7-textarea').value = '';
    localStorage.removeItem('column2-8-textarea');
    document.getElementById('column2-8-textarea').value = '';
    localStorage.removeItem('column2-9-textarea');
    document.getElementById('column2-9-textarea').value = '';
  
    localStorage.removeItem('column3-1-textarea');
    document.getElementById('column3-1-textarea').value = '';
    localStorage.removeItem('column3-2-textarea');
    document.getElementById('column3-2-textarea').value = '';
    localStorage.removeItem('column3-3-textarea');
    document.getElementById('column3-3-textarea').value = '';
    localStorage.removeItem('column3-4-textarea');
    document.getElementById('column3-4-textarea').value = '';
    localStorage.removeItem('column3-5-textarea');
    document.getElementById('column3-5-textarea').value = '';
    localStorage.removeItem('column3-6-textarea');
    document.getElementById('column3-6-textarea').value = '';
    localStorage.removeItem('column3-7-textarea');
    document.getElementById('column3-7-textarea').value = '';
    localStorage.removeItem('column3-8-textarea');
    document.getElementById('column3-8-textarea').value = '';
    localStorage.removeItem('column3-9-textarea');
    document.getElementById('column3-9-textarea').value = '';
  
    localStorage.removeItem('column4-1-textarea');
    document.getElementById('column4-1-textarea').value = '';
    localStorage.removeItem('column4-2-textarea');
    document.getElementById('column4-2-textarea').value = '';
    localStorage.removeItem('column4-3-textarea');
    document.getElementById('column4-3-textarea').value = '';
    localStorage.removeItem('column4-4-textarea');
    document.getElementById('column4-4-textarea').value = '';
    localStorage.removeItem('column4-5-textarea');
    document.getElementById('column4-5-textarea').value = '';
    localStorage.removeItem('column4-6-textarea');
    document.getElementById('column4-6-textarea').value = '';
    localStorage.removeItem('column4-7-textarea');
    document.getElementById('column4-7-textarea').value = '';
    localStorage.removeItem('column4-8-textarea');
    document.getElementById('column4-8-textarea').value = '';
    localStorage.removeItem('column4-9-textarea');
    document.getElementById('column4-9-textarea').value = '';
  
    localStorage.removeItem('column5-1-textarea');
    document.getElementById('column5-1-textarea').value = '';
    localStorage.removeItem('column5-2-textarea');
    document.getElementById('column5-2-textarea').value = '';
    localStorage.removeItem('column5-3-textarea');
    document.getElementById('column5-3-textarea').value = '';
    localStorage.removeItem('column5-4-textarea');
    document.getElementById('column5-4-textarea').value = '';
    localStorage.removeItem('column5-5-textarea');
    document.getElementById('column5-5-textarea').value = '';
    localStorage.removeItem('column5-6-textarea');
    document.getElementById('column5-6-textarea').value = '';
    localStorage.removeItem('column5-7-textarea');
    document.getElementById('column5-7-textarea').value = '';
    localStorage.removeItem('column5-8-textarea');
    document.getElementById('column5-8-textarea').value = '';
    localStorage.removeItem('column5-9-textarea');
    document.getElementById('column5-9-textarea').value = '';
  
    localStorage.removeItem('column6-1-textarea');
    document.getElementById('column6-1-textarea').value = '';
    localStorage.removeItem('column6-2-textarea');
    document.getElementById('column6-2-textarea').value = '';
    localStorage.removeItem('column6-3-textarea');
    document.getElementById('column6-3-textarea').value = '';
    localStorage.removeItem('column6-4-textarea');
    document.getElementById('column6-4-textarea').value = '';
    localStorage.removeItem('column6-5-textarea');
    document.getElementById('column6-5-textarea').value = '';
    localStorage.removeItem('column6-6-textarea');
    document.getElementById('column6-6-textarea').value = '';
    localStorage.removeItem('column6-7-textarea');
    document.getElementById('column6-7-textarea').value = '';
    localStorage.removeItem('column6-8-textarea');
    document.getElementById('column6-8-textarea').value = '';
    localStorage.removeItem('column6-9-textarea');
    document.getElementById('column6-9-textarea').value = '';
  
    localStorage.removeItem('column7-1-textarea');
    document.getElementById('column7-1-textarea').value = '';
    localStorage.removeItem('column7-2-textarea');
    document.getElementById('column7-2-textarea').value = '';
    localStorage.removeItem('column7-3-textarea');
    document.getElementById('column7-3-textarea').value = '';
    localStorage.removeItem('column7-4-textarea');
    document.getElementById('column7-4-textarea').value = '';
    localStorage.removeItem('column7-5-textarea');
    document.getElementById('column7-5-textarea').value = '';
    localStorage.removeItem('column7-6-textarea');
    document.getElementById('column7-6-textarea').value = '';
    localStorage.removeItem('column7-7-textarea');
    document.getElementById('column7-7-textarea').value = '';
    localStorage.removeItem('column7-8-textarea');
    document.getElementById('column7-8-textarea').value = '';
    localStorage.removeItem('column7-9-textarea');
    document.getElementById('column7-9-textarea').value = '';
  
    localStorage.removeItem('column8-1-textarea');
    document.getElementById('column8-1-textarea').value = '';
    localStorage.removeItem('column8-2-textarea');
    document.getElementById('column8-2-textarea').value = '';
    localStorage.removeItem('column8-3-textarea');
    document.getElementById('column8-3-textarea').value = '';
    localStorage.removeItem('column8-4-textarea');
    document.getElementById('column8-4-textarea').value = '';
    localStorage.removeItem('column8-5-textarea');
    document.getElementById('column8-5-textarea').value = '';
    localStorage.removeItem('column8-6-textarea');
    document.getElementById('column8-6-textarea').value = '';
    localStorage.removeItem('column8-7-textarea');
    document.getElementById('column8-7-textarea').value = '';
    localStorage.removeItem('column8-8-textarea');
    document.getElementById('column8-8-textarea').value = '';
    localStorage.removeItem('column8-9-textarea');
    document.getElementById('column8-9-textarea').value = '';
  
    localStorage.removeItem('column9-1-textarea');
    document.getElementById('column9-1-textarea').value = '';
    localStorage.removeItem('column9-2-textarea');
    document.getElementById('column9-2-textarea').value = '';
    localStorage.removeItem('column9-3-textarea');
    document.getElementById('column9-3-textarea').value = '';
    localStorage.removeItem('column9-4-textarea');
    document.getElementById('column9-4-textarea').value = '';
    localStorage.removeItem('column9-5-textarea');
    document.getElementById('column9-5-textarea').value = '';
    localStorage.removeItem('column9-6-textarea');
    document.getElementById('column9-6-textarea').value = '';
    localStorage.removeItem('column9-7-textarea');
    document.getElementById('column9-7-textarea').value = '';
    localStorage.removeItem('column9-8-textarea');
    document.getElementById('column9-8-textarea').value = '';
    localStorage.removeItem('column9-9-textarea');
    document.getElementById('column9-9-textarea').value = '';
  }