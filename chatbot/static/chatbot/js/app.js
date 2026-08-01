/* ==========================================================
   ABC BANK SMARTASSIST
   FRONTEND JAVASCRIPT
========================================================== */


/* ==========================================================
   AUTO SCROLL
========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    const conversation = document.getElementById("conversation");

    if (conversation) {

        conversation.scrollTop = conversation.scrollHeight;

    }

});


/* ==========================================================
   QUICK ACTIONS
========================================================== */

function setQuestion(question) {

    const input = document.getElementById("message");

    input.value = question;

    input.focus();

}


/* ==========================================================
   CLEAR INPUT
========================================================== */

function clearInput() {

    document.getElementById("message").value = "";

    document.getElementById("message").focus();

}


/* ==========================================================
   LOADING
========================================================== */

function showLoading() {

    const loading = document.getElementById("loading");

    const sendBtn = document.getElementById("sendBtn");

    if (loading) {

        loading.style.display = "flex";

    }

    if (sendBtn) {

        sendBtn.disabled = true;

        sendBtn.innerHTML = "Sending...";

    }

}


/* ==========================================================
   VOICE INPUT
========================================================== */

function startListening() {

    if (!('webkitSpeechRecognition' in window)) {

        alert("Voice recognition is not supported in this browser.");

        return;

    }

    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-US";

    recognition.interimResults = false;

    recognition.maxAlternatives = 1;

    recognition.start();

    recognition.onresult = function (event) {

        document.getElementById("message").value =
            event.results[0][0].transcript;

    };

    recognition.onerror = function () {

        alert("Voice recognition failed.");

    };

}


/* ==========================================================
   TEXT TO SPEECH
========================================================== */

function speakResponse() {

    const responses = document.getElementsByClassName("bot-response");

    if (responses.length === 0) {

        return;

    }

    const lastResponse = responses[responses.length - 1].innerText;

    speechSynthesis.cancel();

    const speech = new SpeechSynthesisUtterance(lastResponse);

    speech.lang = "en-US";

    speech.rate = 1;

    speech.pitch = 1;

    speech.volume = 1;

    speechSynthesis.speak(speech);

}


/* ==========================================================
   ENTER TO SEND
========================================================== */

const messageBox = document.getElementById("message");

if (messageBox) {

    messageBox.addEventListener("keydown", function (event) {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            document.getElementById("chatForm").submit();

        }

    });

}
/* ==========================================================
   FEEDBACK
========================================================== */

function submitFeedback(rating){

    fetch("/feedback/",{

        method:"POST",

        headers:{

            "Content-Type":"application/x-www-form-urlencoded",

            "X-CSRFToken":getCookie("csrftoken")

        },

        body:

            "chat_id=" + chatId +

            "&rating=" + rating +

            "&comment="

    })

    .then(response=>response.json())

    .then(data=>{

        if(data.success){

            alert("Thank you for your feedback!");

        }else{

            alert("Unable to save feedback.");

        }

    });

}


/* CSRF */

function getCookie(name){

    let cookieValue=null;

    if(document.cookie && document.cookie!==""){

        const cookies=document.cookie.split(";");

        for(let i=0;i<cookies.length;i++){

            const cookie=cookies[i].trim();

            if(cookie.substring(0,name.length+1)===name+"="){

                cookieValue=decodeURIComponent(

                    cookie.substring(name.length+1)

                );

                break;

            }

        }

    }

    return cookieValue;

}