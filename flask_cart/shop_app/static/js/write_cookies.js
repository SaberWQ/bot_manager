const listButtons = document.querySelectorAll(".buy")

for (let count = 0; count < listButtons.length; count++) {
    let button = listButtons[count]
    button.addEventListener(
        type = "click",
        listener = function (event) {
            if (document.cookie == ""){
                document.cookie = `products = ${button.id}; path = /`
            }
            else{
                productId = document.cookie.split("=")[1]
                document.cookie = `products = ${productId} ${button.id}; path = /`
            }
        }
    )
}