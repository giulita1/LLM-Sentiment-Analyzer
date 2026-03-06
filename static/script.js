const input = document.getElementById('input-coment');
const btn = document.getElementById('btn-send');
const pResponse = document.getElementById('p-response');
const container = document.querySelector('.container');

btn.addEventListener("click", enviar);

async function enviar() {

    const text = input.value;

    if(!text){ 
        alert("Please write a comment");
        return; }
    try{
    const response = await fetch('/coment',{
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({text: text})
    });

    if(!response.ok){
        const errorData = await response.json();
        pResponse.textContent = `Error: ${errorData.detail}`;
        return;
    }
    
    const data = await response.json();

    pResponse.textContent = data.predictions;

    container.classList.add('active');

    }catch(error){
        console.error("error", error);
        pResponse.textContent="Error";
    }

};

input.addEventListener("keydown", function(e){
    if(e.key=="Enter"){
        enviar();
    }
})