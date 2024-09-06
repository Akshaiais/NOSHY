function loginvalidation(){
    
    uname=document.getElementById('uname').value
    password=document.getElementById('password').value
    if (uname==""){
        document.getElementById('msg1').innerHTML='"please enter Username"'
        return false
    }else if(password==""){
        document.getElementById('msg2').innerHTML='"please enter Password"'
        return false
    }else{
        return true
    }
}