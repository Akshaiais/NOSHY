function registervalidation(){
    hname=document.getElementById('hname').value
    address=document.getElementById('address').value
    image=document.getElementById('image').value
    email=document.getElementById('email').value
    mobile=document.getElementById('mobile').value
    password=document.getElementById('password').value
    confirm_password=document.getElementById('confirm_password').value
    if (hname==""){
        document.getElementById('msg1').innerHTML='"please enter restaurant name"'
        return false
    }else if(address==""){
        document.getElementById('msg2').innerHTML='"please enter adress"'
        return false
    }else if(image==""){
        document.getElementById('msg3').innerHTML='"please upload restaurant image"'
        return false
    }else if(email==""){
        document.getElementById('msg4').innerHTML='"please enter email adress"'
        return false
    }else if(mobile==""){
        document.getElementById('msg5').innerHTML='"please enter mobile number"'
        return false
    }else if(password==""){
        document.getElementById('msg6').innerHTML='"please enter password"'
        return false
    }else if(password!=confirm_password){
        document.getElementById('msg7').innerHTML='"should be match with password"'
        return false
    }else{
        return true
    }
}