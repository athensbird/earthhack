{
  "GCLOUD_PROJECT": "intuithome",
  "DATA_BACKEND": "cloudsql",
  "MYSQL_USER": "root",
  "MYSQL_PASSWORD": "aggieHack",
  "INSTANCE_CONNECTION_NAME": "intuithome:us-central1:intuit-home"
}

./cloud_sql_proxy -instances="intuithome:us-central1:intuit-home"=tcp:3306
