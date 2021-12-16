function name(){
    var ret = prompt("이름을 입력하세요", "이호영");
    if(ret==null){
        
    }
    else if(ret ==""){
        var response = confirm("다시 입력해주세요");
        if (response==true){
            name();
        }
        else{
          
        }
    }
    else{
        var response = confirm(`${ret}가 맞습니까?`);
        if (response==true){
            alert(`환영합니다! ${ret}님!! `);
        }
        else{
           name();
        }
    }
}
name();