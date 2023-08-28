const loadBtn = document.getElementById('load-invite') 
const loadBox = document.getElementById('namer')

const handleGet = () => {
    $.ajax(
        {
            type: 'GET',
            url: '/user_profile/',
            success: function(response){
                console.log(response)
                loadBox.innerHTML += '<div id="namer-input"><input type="text" name="namername" placeholder="Type your name"></div><div class="namer-controls"><div><button>OK</button></div></div>'
            },
            error: function(error){
                console.log(error)
            }
        }
    )
}

