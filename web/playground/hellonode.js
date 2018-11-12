// Load HTTP module
const http = require("http");
const hostname = '127.0.0.1';
const port = 5000;

// Create HTTP server and listen on port 3000 for requests
const server = http.createServer((req, res) => {
    // Set the response HTTP header with HTTP status and content type
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello world\n');
});

// Listen for request on port 3000, and as a callback function have the port listened on logged
server.listen(port, hostname, () => {
    console.log(`Server running at https://${hostname}:${port}/`);
});