let messageURL = 'http://127.0.0.1:5000/message'
let welcomedUser = false

function sendMessage(payload) {
  addMessage(payload.message)
  $('#textarea').val('')
  $.post(messageURL, payload, function (data) {
    addMessage(data.response, true)
  })
}

function addMessage(message, isBot) {
  let classes = isBot ? 'single_message single_message_bot' : 'single_message'
  let txt = $('<p></p>').text(message).addClass(classes)
  $('#message_box').append(txt)
}

$.when($.ready).then(function () {
  // On enter event
  $('#textarea').keydown(function (event) {
    // if 'Enter' is clicked
    if (event.which === 13) {
      let message = $('#textarea').val()
      sendMessage({ message })
    }
  })

  $('#modal_close').bind('click', function () {
    $('#modal').hide()
    $('#chatNow').show()
  })

  $('#chatNow').bind('click', function () {
    $('#modal').slideToggle()
    $('#chatNow').hide()
    if (!welcomedUser) {
      setTimeout(() => {
        welcomedUser = true
        addMessage('Hi there! How can I help today?', true)
      }, 2000)
    }
  })

  $('#chat_form').on('submit', function (e) {
    e.preventDefault()
    let message = $('#textarea').val()
    sendMessage({ message })
  })
})
