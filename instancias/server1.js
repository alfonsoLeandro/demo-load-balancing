const express = require('express');
const app = express();

app.get('/', function (req, res) {
    res.status(200).send('App 1 respondiendo!!!');
});

const port = 3001;

const server = app.listen(port, function() {
    console.log('Express server listening on port ' + port);
});