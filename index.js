// Importa o Módulo Express (Nescessário)
const express = require('express');

// Cria o Servidor
const server = express();


// A Lógica do Tester
server.get('/http/response/:reponseType', (req, res) => {
    const responseType = req.params.reponseType;
    res.status(responseType).send(responseType);
    console.log(responseType);
});

const port = 7620

// Coloca o Servidor de Pé
server.listen(port, () => {
    console.log(`Server em: http://localhost:${port}/`);
    console.log(`Teste em: http://localhost:${port}/200`);
    console.log('Ctrl+C Para Chutar o Servidor');
});