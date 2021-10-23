let messageURL = 'http://127.0.0.1:5000/message'

function sendMessage(payload) {
  $.post(messageURL, payload, function (data, status) {})
  addMessage(payload.message)
}

function addMessage(message, isBot) {
  let classes = isBot ? 'single_message single_message_bot' : 'single_message'
  let txt = $('<p></p>').text(message).addClass(classes)
  $('#message_box').append(txt)
}

$.when($.ready).then(function () {
  $('#modal_close').bind('click', function () {
    $('#backdrop').hide()
    $('#modal').hide()
  })

  $('#chatNow').bind('click', function () {
    $('#backdrop').show()
    $('#modal').show()
  })

  $('#chat_form').on('submit', function (e) {
    e.preventDefault()
    let message = $('#textarea').val()
    sendMessage({ message })
    $('#backdrop').hide()
    $('#modal').hide()
  })
})
