
function contact(form){
    const formData = {
        name: form.querySelector('[name=name]').value,
        email: form.querySelector('[name=email]').value,
        phone_no: form.querySelector('[name=phone_no]').value,
        description: form.querySelector('[name=description]').value
    }
    const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value
    const nameReTest = /^([a-zA-Za-яё]\s?)+$/.test(formData.name) ;
    const emailReTest = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/.test(formData.email);
    const phoneReTest = /^((8|\+7)[\- ]?)?9(\(?\d{2}\)?[\- ]?)?[\d\- ]{7,10}$/.test(formData.phone_no)

    if (nameReTest && emailReTest && phoneReTest){
        console.log('Test passed')
        let resp = sendContactReq(formData, csrfToken)
        console.log(resp)
    } else {
        if (!nameReTest){
            console.log('name failed test')
        }
        if (!emailReTest){
            console.log('email failed test')
        }
        if (!phoneReTest){
            console.log('phone failed test')
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