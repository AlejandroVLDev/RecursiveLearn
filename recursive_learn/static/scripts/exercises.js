let number = 0;
var counter = -1;
var auxCounter = 0;

const button_end = document.querySelector(".end");

const first = document.getElementById("primero");
const paragraph = document.getElementById("paragraph_content");
const content = document.getElementById("content");
const code_block = document.getElementById("code_content");

var paragraphs = parse(document.getElementById("paragraph").value);
var options = parse(document.getElementById("options").value);
var code = parse(document.getElementById("code").value);
var optionsChange = parse(replaceBool(document.getElementById("optionsChange").value));
const place = document.getElementById("place").value;
const code_recursive = parse(document.getElementById("code_recursive").value);
var paragraph1 = parse(document.getElementById("paragraph1").value);
var options1 = parse(document.getElementById("options1").value);
var code1 = parse(document.getElementById("code1").value);
var optionsChange1 = parse(replaceBool(document.getElementById("optionsChange1").value));
var paragraph2 = parse(document.getElementById("paragraph2").value);
var options2 = parse(document.getElementById("options2").value);
var code2 = parse(document.getElementById("code2").value);
var optionsChange2 = parse(replaceBool(document.getElementById("optionsChange2").value));

addGlobalEventListener('click', '.back', e => {
    bocadillo(-1);
})

addGlobalEventListener('click', '.next1', e => {
    bocadillo(1);
})

addGlobalEventListener('click', '.next2', e => {
    bocadillo(2);
})

addGlobalEventListener('click', '.next3', e => {
    bocadillo(3);
})

addGlobalEventListener('click', '.hardnext1', e => {
    number = 1;
    paragraphs = paragraph1;
    options = options1;
    code = code1;
    optionsChange = optionsChange1;
    counter = -1;
    bocadillo(1);
})

addGlobalEventListener('click', '.hardnext2', e => {
    number = 2;
    paragraphs = paragraph2;
    options = options2;
    code = code2;
    optionsChange = optionsChange2;
    counter = -1;
    bocadillo(1);
})

addGlobalEventListener('click', '.nextstage1', e => {
    number = 1;
    code[place] = code_recursive[0];
    bocadillo(1);
})

addGlobalEventListener('click', '.nextstage2', e => {
    number = 2;
    code[place] = code_recursive[1];
    bocadillo(1);
})

addGlobalEventListener('click', '.nextstage3', e => {
    number = 3;
    code[place] = code_recursive[2];
    bocadillo(1);
})

addGlobalEventListener('click', '.evaluate', e => {
    calculate();
})

addGlobalEventListener('click', '.end_exercise', e => {
    button_end.removeAttribute('disabled');
    const container_button_end = document.querySelector('.badge_container');
    container_button_end.classList.add('end_active');
})

async function calculate(){
    const valuePara = paragraph.innerHTML;
    const valueContent = content.innerHTML;
    const first = document.getElementById("first");
    const second = document.getElementById("second");
    const title = document.querySelector(".title");
    let datax = {'first': first.value, 'number': number, 'title': title.innerHTML, 'aux_counter': auxCounter};
    if (second){
        datax['second'] = second.value;
    }
    espera();
    const result = await logJSONData(datax);
    if (result.error){
        paragraph.innerHTML = valuePara;
        content.innerHTML = valueContent;
        alert(result.error);
    } else {
        const subproblem_element = document.getElementById("subproblem");
        subproblem_element.innerHTML = result.subproblem;
        const simpler_element = document.getElementById("simpler");
        simpler_element.innerHTML = result.simple_solution;
        const result_element = document.getElementById("result");
        result_element.innerHTML = result.result;
        auxCounter += 1;
        bocadillo(1);
    }
}

function addGlobalEventListener(type, selector, callback) {
    document.addEventListener(type, e =>{
        if (e.target.matches(selector)) callback(e);
    })
}

function bocadillo(number) {
    if (number < 0) {
        counter -= 1;
        number *= -1;
    } else {
        counter += 1;
    }
    number -= 1;
    addParagraph(number);
    addOptions(number);
    addCode(number);
}

function addParagraph(number) {
    paragraph.innerHTML = paragraphs[counter][number];
}

function addOptions(number) {
    if (optionsChange[counter]) {
        content.classList.remove('next-content');
        content.classList.add('options');
    } else {
        content.classList.add('next-content');
        content.classList.remove('options');
    }
    content.innerHTML = options[counter][number];
}

function addCode(number) {
    if (code[counter][number] != void[0]){
        if(code[counter][number] != ['']){
            const delete_code = document.querySelector(".delete");
            if (delete_code){
                delete_code.remove();
            }
            code_block.innerHTML += code[counter][number];
            code[counter][number] = '';
        }
    }
}

function espera() {
    paragraph.innerHTML = "Se está calculando el resultado, espere.";
    content.innerHTML = "";
}

first.addEventListener("click", ()=> {
    const ring = document.querySelector(".r1");
    const outline = document.querySelector(".o1");
    const ring_stick = document.querySelector(".s1");
    ring.classList.add("focus");
    ring_stick.classList.add("focus-stick");
    outline.classList.add("focus-border");
});


async function logJSONData(data) {
    const response = await fetch("http://127.0.0.1:8000/exercises/getresults/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    const jsonData = await response.json();
    return jsonData;
}

function replaceBool(data) {
    data = data.replaceAll('True', 'true');
    return data.replaceAll('False', 'false');
}

function parse(data) {
    if (data != ''){
        data = data.replaceAll('\"', '\\"');
        data = data.replaceAll("'", '"');
        return JSON.parse(data);
    }
    return []
}
