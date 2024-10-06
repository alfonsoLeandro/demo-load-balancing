const express = require('express');
const app = express();

app.get('/', function (req, res) {
    res.status(200).send('si el 2 anda bien');
});

const port = 3002;

const server = app.listen(port, function() {
    console.log('Express server listening on port ' + port);
});