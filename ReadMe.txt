Developed using SwaggerHub
Code is found in swagger_server/controllers/default_controller.py

To run on docker, from (Receipt_Challenge/Receipt_Challenge) run:

bash
# building the image
docker build -t swagger_server .
# starting up a container
docker run -p 8080:8080 swagger_server
URL is http://localhost:8080/poa-480/dfad/1.0.0/ui/#/default/receipts_id_points_get



Print statements were left intentionally to aid with reviewing
