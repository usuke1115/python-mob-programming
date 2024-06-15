const copyButtons = document.getElementsByClassName("copy__btn");
const shortenUrls = document.getElementsByClassName("shorten__url");

const changeButtonText = async (button, intervalSeconds=1000, text="copy") => {
    setTimeout(() => {
        button.innerHTML = text;
    }, intervalSeconds);
}

for (let i = 0; i < copyButtons.length; i++) {
    const clickedButton = copyButtons[i];
    const text = shortenUrls[i].textContent;
    clickedButton.addEventListener("click", async () => {
        await navigator.clipboard
            .writeText(text)
            .then(() => {
                    clickedButton.innerHTML = "copied!";
                    changeButtonText(clickedButton);
                }, () => {
                    clickedButton.innerHTML = "No!";
                    changeButtonText(clickedButton);
                });
    });
};
