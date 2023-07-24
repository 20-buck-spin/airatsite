
function contact(form){
    const forbiddenChars = ['<', '>', '{', '}', '#', '^', '~', '|', '*']
    const formData = {
        name: form.querySelector('[name=name]').value,
        email: form.querySelector('[name=email]').value,
        phone_no: form.querySelector('[name=phone_no]').value,
        description: form.querySelector('[name=description]').value
    }

    let formHasEmtpy = false
    for (let key in formData){
        if (formData[key] == '' || formData[key] == null){
            console.log(`a ${formData[key]}`)
            errMsg = "Поле Обязательное"
            formHasEmtpy = true
            ShowContactFormFieldError(form, key, errMsg)
        }
    }

    if (formHasEmtpy){
        return null
    }

    const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value
    const nameReTest = /^([a-zA-Za-яё]\s?)+$/.test(formData.name) ;
    const emailReTest = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/.test(formData.email);
    const phoneReTest = /^((8|\+7)[\- ]?)?9(\(?\d{2}\)?[\- ]?)?[\d\- ]{7,10}$/.test(formData.phone_no)
    const descriptionReTest = !forbiddenChars.some(char => formData.description.includes(char))

    if (nameReTest && emailReTest && phoneReTest && descriptionReTest){
        console.log('Test passed')

        let resp = sendContactReq(formData, csrfToken)
            .then(response => {
            clearContactForm()

            if (response.status == 'Success') {
                location.href = '/orders/order_confirmation'
            }

            })


    } else {
        if (!nameReTest){
            let errMsg = 'Только Русские и Латинские букви доступны'
            ShowContactFormFieldError(form, 'name', errMsg)
        }
        if (!emailReTest){
            let errMsg = 'Почта неправильно указана'
            ShowContactFormFieldError(form, 'email', errMsg)
        }
        if (!phoneReTest){
            let errMsg = 'Номер неправильно указана'
            ShowContactFormFieldError(form, 'phone_no', errMsg)
        }
        if (!descriptionReTest){
            let errMsg = `В тексте не разрешаются симболы ${forbiddenChars.toString().slice(1,-1)}`
            ShowContactFormFieldError(form, 'phone_no', errMsg)
        }
    }
}

async function sendContactReq(formData, csrf){
    const contactReqHeaders = {'X-CSRFToken': csrf,
                               'Content-Type': "application/json"
                              }
    let res = await fetch('http://127.0.0.1:8000/orders/create_order', {
        method: 'POST',
        headers: contactReqHeaders,
        mode: 'same-origin',
        body: JSON.stringify(formData)
    })

    let res_json = await res.json()
    return res_json
}


function ShowContactFormFieldError(form, fieldName, errorMsg){
    let error = form.querySelector(`[name=${fieldName}]`).nextElementSibling
            error.innerText  = errorMsg
            error.style.display = 'block'
}

function clearContactForm(){
    console.log('clearing form')
    let form = document.querySelector("#contact-form")
    let inputFields = form.querySelectorAll("input, textarea")
    Array.from(inputFields).forEach(inputField => {
        inputField.value = ''
    })

    let errorMsges = form.querySelectorAll(".field-error")
    Array.from(errorMsges).forEach(errorMsg => {
        errorMsg.innerText  = ''
        errorMsg.style.display = 'none'
    })
}

