const input = document.getElementById('input-coment');
const btn = document.getElementById('btn-send');
const pResponse = document.getElementById('p-response');
const container = document.querySelector('.container');
btn.addEventListener("click", async ()=> {

    const text = input.value;
    if(!text){ return; }
    try{
    const response = await fetch('/coment',{
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({comment: text})
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
});

