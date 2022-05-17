// const http = require('http');
const express = require('express');
const app = express();
const port = 8080;
const cors = require('cors');

app.use(cors())

// using nodejs and node-fetch

const fetch = require('node-fetch');
const { text } = require('express');
// const fs = require('fs');

var myHeaders = new fetch.Headers();
myHeaders.append("Authorization", "Bearer AAAAAAAAAAAAAAAAAAAAAC3qYwEAAAAATi7Fx3%2BYafp46A1qkrErUrTN%2BU8%3DL7qKcgruEaSiHbSi7lPP0N8Qm0HVYmJAeVDQXS8s6sl9PWTokK");
myHeaders.append("Cookie", "guest_id=v1%3A164425973616660343");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

async function retrieveTweets() {
  const response = await fetch("https://api.twitter.com/2/tweets/search/recent?tweet.fields=created_at,lang&media.fields=preview_image_url&max_results=10&query=blockchain", requestOptions)
    /*.then(response => response.json())
    /*.then(result => console.log(result.data[0]['text']))*/
  return response.json();
}

/*
// Creates server instance
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.write('Hello World!');
  res.end();
}).listen(8080);*/

app.get('/', async (req, res) => {
  const tweets = await retrieveTweets()

  res.send(tweets);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
