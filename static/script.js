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

   const predictions = data.predictions;

pResponse.innerHTML = "<b>Detected emotions</b>";

const grid = document.createElement("div");
grid.classList.add("emotion-grid");

let delay =0;

for (const emotion in predictions) {

    const porcentaje = (predictions[emotion] * 100).toFixed(1);

    const card = document.createElement("div");
    card.classList.add("emotion-card");

    const label = document.createElement("div");
    label.classList.add("emotion-name");
    label.textContent = emotion;

    const valor = document.createElement("div");
    valor.classList.add("emotion-percent");
    valor.textContent = porcentaje + "%";

    card.appendChild(label);
    card.appendChild(valor);

    setTimeout(() => {
        card.classList.add("show");
    }, delay);

    delay += 120;

    grid.appendChild(card);
}

pResponse.appendChild(grid);

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