

function getInputValue(){
    // Selecting the input element and get its value 
    
    var inputVal = document.getElementById("howudoin").value;
    var score = 0
    var output = document.getElementById('output');   
    var user_name = "patel.maan14@gmail.com"
    var password = "Maan_2000"

    console.log("hellosidkjf")
        // Displaying the value
    let access_token = "eyJraWQiOiI1RDVOdFM1UHJBajVlSlVOK1RraXVEZE15WWVMMFJQZ3RaUDJGTlhESHpzPSIsImFsZyI6IlJTMjU2In0.eyJjdXN0b206Y291bnRyeSI6IkNBIiwic3ViIjoiZjY5M2YyMGItYmY2Yi00OTc3LWFjYWMtMGM3YjVmMjhhOGVjIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImN1c3RvbTpwZXJzb25hbGl6YXRpb25BdXRoIjoiMSIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbVwvZXUtd2VzdC0xX0FVSGdRMDhDQiIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiJmNjkzZjIwYi1iZjZiLTQ5NzctYWNhYy0wYzdiNWYyOGE4ZWMiLCJjdXN0b206Y29tcGFueSI6IlN0dWRlbnQiLCJhdWQiOiIxZWdzNjNxOTlwM3NlYmVjaHNiNzI5dDgwbyIsImV2ZW50X2lkIjoiMDBjMWE3NGYtYmZjMS00MjA2LTg0ZjEtYmIzZDliZjdhYmM2IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjMxNzE2MjksIm5hbWUiOiJNYWFuIiwicGhvbmVfbnVtYmVyIjoiKzE0MTY4ODkxNDE4IiwiZXhwIjoxNjI1MTA2MDIxLCJpYXQiOjE2MjUwMTk2MjEsImZhbWlseV9uYW1lIjoiUGF0ZWwiLCJlbWFpbCI6InBhdGVsLm1hYW4xNEBnbWFpbC5jb20iLCJjdXN0b206bWFya2V0aW5nQXV0aCI6IjEifQ.YK1a3XxhmeefXtOsE0La_TxRLChFT71lUprej2hEq1WWwQy8NcHOQTWRCze8aWuR7HUfBaRPZxa24wvg758nGifm3FYD-qkjtSofXg0f1GlmLj8y1AkxN8BQILcLGm4yWiXruR5LUZ76segsfm8pgkJSfiBoLKC15A11I7gkb2X2K8EuPhChlIQKfmHQTdYYNTGSItbW3C0A-dyySVcQgpa2f_2NwB59Tt0YY9OYY0iIGqfYIJNA1nrMMpIV9op_hNQVwXA9oNTNuC4Y2MeLB_zjjSU51o8qiIinZAxVMNG6mArMYd6h1y2FX9K9Z6-i_4ZGP75DbitQbfxx_bm61g"

    let request = new XMLHttpRequest();
    request.responseType = "json";
    request.open('POST', "https://nlapi.expert.ai/v2/analyze/standard/en/sentiment");
    request.setRequestHeader("Authorization", "Basic " + btoa(user_name + ":" + password));
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.onload = function () {
    // do something to response
    /* var type = XMLHttpRequest.responseType */
    score = request.response.data.sentiment.overall;
    console.log(request.response.data.sentiment.overall);
    if (score < 0) {
    output.innerHTML = "It seems that you are not in favor of the stock. I will give you a bearish sentiment of Sell. &#128550;"
    }
    else if (score > 0){
    output.innerHTML = "It seems that you are in favor of the stock. I will give you a Bullish Sentiment of Buy! &#128516;"
    }
    else {
    output.innerHTML = "Hmm.. I'm not sure about that. You don't seem to support nor go against the stock. &#129300;"
    }
    };
    request.send(JSON.stringify({
    "document": {
    "text": document.getElementById("howudoin").value
    }
    }));
    score = request.response.data.sentiment.overall;
    console.log(score)
}
