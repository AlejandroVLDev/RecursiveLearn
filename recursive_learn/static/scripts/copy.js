const copy_button = document.getElementById("copy");
copy_button.addEventListener("click", () =>{
    const copyText = document.getElementById("code_content").innerText;
    const copyTag = document.getElementById("copy_text");
    const final = copyText.replace(/\u00A0/g, ' ');
    copy_button.disabled = true;
     // Copy the text inside the text field
    navigator.clipboard.writeText(final);
    copyTag.innerHTML = "Copiado";
    copy_button.classList.add("appear");
    setTimeout(()=>{ copy_button.classList.remove("appear"); copy_button.disabled = false;}, 6000);
})
