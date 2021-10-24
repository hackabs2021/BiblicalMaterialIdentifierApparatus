let messageURL = 'http://127.0.0.1:5000/message'
let welcomedUser = false

function clearTextField() {
  setTimeout(() => {
    $('#textarea').val('')
  }, 300)
}

function sendMessage(payload) {
  addMessage(payload.message)
  clearTextField()
  $.post(messageURL, payload, function (data) {
    addMessage(data.response, true)
  })
}

function addMessage(message, isBot) {
  let classes = isBot ? 'single_message single_message_bot' : 'single_message'
  let containerClasses = isBot
    ? 'message_container message_container_bot'
    : 'message_container'
  let txt = $('<p></p>').text(message).addClass(classes)
  let sender = $('<i></i>').text(isBot ? 'Bot' : 'You')
  let container = $('<div></div>')
    .html([sender, txt])
    .addClass(containerClasses)
  $('#message_box').append(container)
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
