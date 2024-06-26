let listOfButtonsImages = document.querySelectorAll('.edit-image')

for (let count = 0; count < listOfButtonsImages.length; count++){
    let button = listOfButtonsImages[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_image = document.querySelector(".input-data")
            input_image.type = "file"
            input_image.name = "image"
            input_image.accept = "image/*"
        }
    )
}

let listOfButtonsNames = document.querySelectorAll('.edit-name')

for (let count = 0; count < listOfButtonsNames.length; count++){
    let button = listOfButtonsNames[count]

    button.addEventListener(
        type = 'click',
        listener = (event) => {
            document.querySelector('.modal-window').style.display = 'flex'
            let input_image = document.querySelector(".input-data")
            input_image.type = "text"
            input_image.name = "name"
            input_image.placeholder = "Задайте нове ім'я"
        }
    )
}