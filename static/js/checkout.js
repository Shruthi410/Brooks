    var total = '{{ order.get_cart_total }}'
    var form = document.getElementById('form')
    form.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form Submitted...')
        document.getElementById('form-button').classList.add("hidden");
        document.getElementById('payment-info').classList.remove("hidden");

    })

    document.getElementById('make-payment').addEventListener('click', function(e){
        submitFormData()
    })

    function submitFormData(){
        console.log('Payment button clicked')

        var userFormData = {
            'name':null,
            'email':null,
            'total':total,
        }
        var shippingInfo = {
            'address':null,
            'state':null,
            'city':total,
            'zipcode':null,
        }

        shippingInfo.address = form.address.value
        shippingInfo.city = form.address.value
        shippingInfo.state = form.address.value
        shippingInfo.zipcode = form.address.value

        var url = '/process-order/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken,
            },
            body:JSON.stringify({'form': userFormData, 'shipping': shippingInfo })
        })
        .then((response) => response.json())
        .then((data) => {
            console.log('Success:', data);
            alert('Transaction Completed');
            document.getElementById("form").reset();

        })

    }
