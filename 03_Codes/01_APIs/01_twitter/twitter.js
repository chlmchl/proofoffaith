// using JQuery

var settings = {
    "url": "https://api.twitter.com/2/tweets/search/recent?tweet.fields=created_at,lang&media.fields=preview_image_url&max_results=15&query=i feel",
    "method": "GET",
    "timeout": 0,
    "headers": {
      "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAC3qYwEAAAAATi7Fx3%2BYafp46A1qkrErUrTN%2BU8%3DL7qKcgruEaSiHbSi7lPP0N8Qm0HVYmJAeVDQXS8s6sl9PWTokK",
      "Cookie": "guest_id=v1%3A164425973616660343"
    },
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });