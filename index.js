web: node index.js
const express = require('express');
const { ExpressPeerServer } = require('peer');
const app = express();
const server = require('http').Server(app);

const peerServer = ExpressPeerServer(server, {
  path: '/peerjs'
});

app.use('/peerjs', peerServer);
