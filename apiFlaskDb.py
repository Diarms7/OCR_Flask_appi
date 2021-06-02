from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Image

app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/API_REST_FLASK'
}
initialize_db(app)#nous importons le formulaire initialize_db pour initialiser notre db


#nous récupérons tous les objets du Movie document en utilisant Movies.objects()
# et les convertissons en JSON utilisant to_json(). Enfin, nous retournons un Response objet,
# où nous avons défini notre type de réponse application/json.
@app.route('/images')
def get_image():
    images = Image.objects().to_json()
    return Response(images, mimetype="application/json", status=200)


@app.route('/images/<id>')
def get_image(id):
    images = Image.objects.get(id=id).to_json()
    return Response(images, mimetype="application/json", status=200)
#Dans la POST demande, nous obtenons d'abord le JSON que nous envoyons et 
# une demande. Et puis nous chargeons le Movie document avec les champs de notre demande 
# avec Movie(**body). On appelle ** ici l'opérateur de diffusion(propagation) qui s'écrit comme ...en JavaScript 
#Ce qu'il fait, comme son nom l'indique, répand l'objet dict .  
#Movie(**body)devient
# Movie(name="Name of the movie",casts=["a caste"],genres=["a genre"])



@app.route('/images', methods=['POST'])
def put_image(id):
    body = request.get_json()
    image = Image(**body).save() #sauvegarde le document et obtenons son id que nous retournons en réponse.
    id = image.id
    return {'id': str(id)}, 200


#nous obtenons le document Movie correspondant id puis mettre a jour 
@app.route('/images/<id>', methods=['PUT'])
def update_image(id):
    body = request.get_json()
    Image.objects.get(id=id).update(**body)
    return '', 200


#similaire à update_movie()ici, nous obtenons le document Movie correspondant idet le supprimons 
# de la base de données.

@app.route('/images/<id>', methods=['DELETE'])
def delete_image(id):
    Image.objects.get(id=id).delete()
    return '', 200

app.run()