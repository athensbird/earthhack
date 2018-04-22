'use strict';

const { dialogflow } = require('actions-on-google');
const functions = require('firebase-functions');
const app = dialogflow();

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
  if (!err) {
    console.log('rows', rows);
    qryResult = rows;
  }
  else console.log(err);
});

connection.end();

var answer = '';
const NAME_ACTION = 'askform';

app.intent(NAME_ACTION, (conv, params) => {
  console.log('params', params);
  console.log('qryResult', qryResult);
  const formType = params.formtype;
  if (!formType) conv.close('No form type detected!');
  if (formType == '1040') {
    answer = 'Form 1040 (officially, the "U.S. Individual Income Tax Return") is one of three IRS Tax forms used for personal (individual) federal income tax filed with internal revenue service';
  } else if (formType == '1099') {
    answer = 'Form 1099 is one of several IRS tax forms (see the variants section) used in the United States to prepare and file an information return to report various types of income other than wages, salaries, and tips (for which Form W-2 is used instead). The term information return is used in contrast to the term tax return although the latter term is sometimes used colloquially to describe both kinds of returns.';
  } else if (formType == 'w9' || formType == 'W9'){
    answer = 'Form W-9 (officially, the "Request for Taxpayer Identification Number and Certification")[1] is used in the United States income tax system by a third party who must file an information return with the Internal Revenue Service (IRS).[2] It requests the name, address, and taxpayer identification';
  } else {
    answer = 'Sorry, we are not aware of that for now!'
  }
  conv.close(`Okay, so query result is ${qryResult}, and the answer is ${answer}`);
});


exports.intuitHome = functions.https.onRequest(app);
