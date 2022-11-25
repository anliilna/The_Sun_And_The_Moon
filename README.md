# When The Sun Loves The Moon
Ce sera un jeu de plateforme fortement inspiré de Heart Star (un jeux vidéo) et "When The Sun Loves The Moon" (une chanson), où deux personnages Sun et Moon devront s'entre aider pour résoudre des niveaux (si j'arrive à en faire) et se réunir.  

Mon objectif final serai de faire au moins 3 niveaux avec des murs qu'un seul personnage pourra traverser, des objets que les joueurs devront ramasser et des portails de téléportation.  

Je prévois d'ajouter:  
-l'interface du jeu (personnages, obstacles, décor, animations)  
-les mouvements des personnages  
-de la musique (que j'ai modifié en 8-bit avec GXSCC)  
-des niveaux  

classes et méthodes utilisées:  
PERSONNAGES:  
  -class Sun et Moon  
  -animate() ( qui fait l'animation des personnages)  
  -get_status() ( qui prend en compte la position des personnages et détermine s'ils marchent, sautent ou tombent)  
  -apply_gravity()  
  -jump()  
  -update()  
INTERFACE:  
  -class Level  
  -setup_level() (prend en compte les colonnes et lignes de l'écran et implémente les 'tiles' et les joueurs)  
  -win_collision ( qui permet de finir un niveau mais ne marche pas encore)  
  -horizontal_movement_collision() et vertical_movement_collision() ( qui détecte quand les personnages entrent en collision avec un 'tile')  
  

Pour ce projet, j'ai suivi des tutos sur YouTube :  
- https://youtube.com/playlist?list=PL8ui5HK3oSiGXM2Pc2DahNu1xXBf7WQh-  
- https://youtu.be/GMBqjxcKogA  

(Programmé en POO avec pygame sur Mu) 
