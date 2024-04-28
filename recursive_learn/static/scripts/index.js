const block_input = document.querySelector(".block-input");
const block_subproblem = document.querySelector(".block-subproblem");
const block_simpler_solution = document.querySelector(".block-simpler-solution");
const block_solution = document.querySelector(".block-solution");
const explain_input = document.querySelector(".explain-input");
const explain_subproblem = document.querySelector(".explain-subproblem")
const explain_simpler_solution = document.querySelector(".explain-simpler-solution");
const explain_solution = document.querySelector(".explain-solution")
const obscure = document.querySelector(".obscure");

block_input.addEventListener("click", ()=> {
    explain_input.classList.toggle("active");
    obscure.classList.toggle("active");
});
block_subproblem.addEventListener("click", ()=> {
    explain_subproblem.classList.toggle("active");
    obscure.classList.toggle("active");
});
block_simpler_solution.addEventListener("click", ()=> {
    explain_simpler_solution.classList.toggle("active");
    obscure.classList.toggle("active");
});
block_solution.addEventListener("click", ()=> {
    explain_solution.classList.toggle("active");
    obscure.classList.toggle("active");
});
obscure.addEventListener("click", ()=> {
    explain_input.classList.remove("active");
    explain_subproblem.classList.remove("active");
    explain_simpler_solution.classList.remove("active");
    explain_solution.classList.remove("active");
    obscure.classList.toggle("active");
});