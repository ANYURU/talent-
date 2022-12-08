#!/bin/sh

#Add your endpoints below by adding a heading of the endpoint and the endpoint.
echo 'Snippets: '
http http://localhost:8000/api/v1/snippets/ 

echo 'Snippet details: '
http http://localhost:8000/api/v1/snippets/1/
