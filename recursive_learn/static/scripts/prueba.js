const par = document.getElementById('paragraph');
ele = document.getElementById('t_x').value;
ele = ele.replaceAll('\"', '\\"');
ele = ele.replaceAll("'", '"');
const data_t = JSON.parse(ele);
console.log(data_t);
data_t.forEach(el => {
    console.log(el);
    el.forEach(element => {
        par.innerHTML += element;
    });
});
console.log(data_t.value);