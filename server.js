var http = require('http');
var url = require('url');

var neo4j = require('neo4j');
var db = new neo4j.GraphDatabase('http://ec2-54-68-208-190.us-west-2.compute.amazonaws.com:7474');

var query = [
  'MATCH n',
  'RETURN n',
  'LIMIT 10'
].join('\n');

var params = {};

db.query(query, params, function (err, results) {
  if (err) throw err;
  console.log(results)
  var likes = results.map(function (result) {
    return result['other'];
  });
  // ...
});

/*
var routes = {
  "/api/getjson": function(parsedUrl) {
    d = new Date(parsedUrl.query.iso);
    return {
      hour: d.getHours(),
      minute: d.getMinutes(),
      second: d.getSeconds()
    };
  },
  "/api/unixtime": function(parsedUrl) {
    return {unixtime: (new Date(parsedUrl.query.iso)).getTime()};
  }
}

server = http.createServer(function(request, response) {
  parsedUrl = url.parse(request.url, true);
  resource = routes[parsedUrl.pathname];
  if (resource) {
    response.writeHead(200, {"Content-Type": "application/json"});
    response.end(JSON.stringify(resource(parsedUrl)));
  }
  else {
    response.writeHead(404);
    response.end();
  }
});
server.listen(process.argv[2]);*/