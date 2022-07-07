
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
        console.log(resp)
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
    let resp = ''
    const contactReqHeaders = {'X-CSRFToken': csrf}
    await fetch('http://localhost:8000/contact', {
        method: 'POST',
        headers: contactReqHeaders,
        mode: 'same-origin',
        body: JSON.stringify(formData)
    }).then(res => resp=res.data)
    return resp
}


function ShowContactFormFieldError(form, fieldName, errorMsg){
    let error = form.querySelector(`[name=${fieldName}]`).nextElementSibling
            error.innerHTML = errorMsg
            error.style.display = 'block'
}

