$.ajax({
    url: '',
    type: 'POST',
    data : {userName : userName,password: password,...},
    // contentType: 'yourConentType', // ConentType that your are sending. No contentType needed if you just posting as query string parameters.
    success: function(response){
        // do whatever you want with response
     },
    error: function(error){
      console.log(error)
    }
});