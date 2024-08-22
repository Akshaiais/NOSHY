function paymentvalidation(){
    cardnumber=document.getElementById('cardnumber').value
    cardname=document.getElementById('cardname').value
    expiry=document.getElementById('expiry').value
    cvv=document.getElementById('cvv').value
    if (cardnumber==""){
        document.getElementById('msg1').innerHTML='"please enter cardNumber"'
        return false
    }else if(cardname==""){
        document.getElementById('msg2').innerHTML='"please enter cardName"'
        return false
    }else if(expiry==""){
        document.getElementById('msg3').innerHTML='"please enter expiry"'
        return false
    }else if(cvv==""){
        document.getElementById('msg4').innerHTML='"please enter cvv"'
        return false
    }else{
        return true
    }
}