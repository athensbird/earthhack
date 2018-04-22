var mysql = require('mysql');

var connection = mysql.createConnection({
  host: "35.192.2.30",
  user: 'markwang',
  password: 'earthhack',
  database: 'keysandanswers'
});

var qryResult = '';

connection.connect(function(err) {
  if (err) {
    console.error('error connecting: ' + err.stack);
    return;
  }
  console.log('connected as id ' + connection.threadId);
});

connection.query('select count(*) from FAQList', (err, rows, field) => {
  if (!err) qryResult = rows;
  else console.log(err);
});

connection.end();

export qryResult;
