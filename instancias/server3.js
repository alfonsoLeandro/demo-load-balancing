const express = require('express');
const app = express();

app.get('/', function (req, res) {
    res.status(200).send('como anda el 3');
});

const port = 3003;

const server = app.listen(port, function() {
    console.log('Express server listening on port ' + port);
});