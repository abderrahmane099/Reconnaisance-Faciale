import dlib
import scipy.misc
import imageio
import numpy as np
import os

#Recuperer le detecteur de visage a partir du DLib
face_detector = dlib.get_frontal_face_detector()

#Recuperer le detecteur de points de visage
shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#Recuperer le model de reconnaisance de visage
face_recognition_model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

#Degre de tolerance
Tolerance = 0.6

#Fonction encodage visage
def get_face_encodings(path_to_image):
    image = imageio.imread(path_to_image)

    #Detecter visage en utilisant le detecteur de visage
    detected_faces = face_detector(image, 1)

    #Recuperer les points de visage
    shapes_faces = [shape_predictor(image, face) for face in detected_faces]

    return [np.array(face_recognition_model.compute_face_descriptor(image, face_pose, 1)) for face_pose in shapes_faces]


#Fonction qui compare le visage donne a une liste de visage deja presents
def compare_face_encodings(known_faces, face):
    return(np.linalg.norm(known_faces - face, axis=1) <= Tolerance)

#Fonction qui match les visages
def find_match(known_faces, names, face):
    matches = compare_face_encodings(known_faces, face)
    
    #Retourne le nom du premier match
    count = 0
    for match in matches:
        if match:
            return names[count]
        count += 1
        
    return 'Qui êtes-vous '

# Recuperer le chemin de toutes les images connues
image_filenames = filter(lambda x: x.endswith('.jpg'), os.listdir('images/'))

# Ordonner par ordre alphabetique
image_filenames = sorted(image_filenames)

# Recuperer le chemin entier des images
paths_to_images = ['images/' + x for x in image_filenames]

# List des encodages de visages disponibles
face_encodings = []

# boucler sur les images pour avoir l'encodage de chacune
for path_to_image in paths_to_images:
    
    face_encodings_in_image = get_face_encodings(path_to_image)

    
    if len(face_encodings_in_image) != 1:
        print("SVP changez image: " + path_to_image + " - elle possede " + str(len(face_encodings_in_image)) + " visages; elle doit posseder uniquement un !!")
        exit()

    # Append l'encodage du visage que nous avons a ceux deja presents
    face_encodings.append(get_face_encodings(path_to_image)[0])
    
# Recuperer chemin de toutes les images de test
test_filenames = filter(lambda x: x.endswith('.jpg'), os.listdir('test/'))

# Recuperer chemin en entier
paths_to_test_images = ['test/' + x for x in test_filenames]

# Recuperer le nom des personnes en enlevant le .jpg
names = [x[:-4] for x in image_filenames]

# Boucler sur le test pour trouver le match
for path_to_image in paths_to_test_images:
    
    face_encodings_in_image = get_face_encodings(path_to_image)

    
    if len(face_encodings_in_image) != 1:
        print("SVP changez image: " + path_to_image + " - elle possede " + str(len(face_encodings_in_image)) + " visages; elle doit posseder uniquement un !!")
        exit()

    # Trouver match pour l'encodage trouve dans le test
    match = find_match(face_encodings, names, face_encodings_in_image[0])

    # Print chemin de l'image test et le match
    usedVar = 'Bonjour, '+match
    print(usedVar)