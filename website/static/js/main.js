$.when($.ready).then(function () {
  $('#modal_close').bind('click', function () {
    $('#backdrop').hide()
    $('#modal').hide()
  })

  $('#chatNow').bind('click', function () {
    $('#backdrop').show()
    $('#modal').show()
  })
})
