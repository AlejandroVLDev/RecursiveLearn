const profile = document.querySelector(".profile");

if (profile) {
    profile.addEventListener("click", () => {
        document.querySelector(".menu").classList.toggle("menu_active");
    })
}