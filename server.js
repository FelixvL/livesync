const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    console.log("waar");
    res.end('Hallo, wereld!');
});

server.listen(3000, () => {
    console.log('Server draait op http://localhost:3000');
});