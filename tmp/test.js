const http = require('http');

// Create an HTTP server
const server = http.createServer((req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/html'
    });
    res.end(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <a href="http://www.baidu.com">Baidu</a>
  <a href=http://www.google.com>Baidu</a>
</body>
</html>`);
});

server.listen('3001');
