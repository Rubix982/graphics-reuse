I run a cloth-simulation pipeline in Blender (its built-in CPU cloth solver) that dresses 3D figures in South Asian garments: a kameez (long tunic), trousers and a dupatta. Each garment piece is about 5,000 vertices. A garment is draped from its flat sewing pattern: the pieces are placed around the body, the seams are closed, and the cloth falls and settles under gravity. One drape takes about 4–7 minutes.

A garment that has already settled on one body is often draped again, from its flat pattern, on a different body (for example a figure 1.609 m tall and one 1.753 m tall). One step of the pipeline re-drapes every garment on a standard figure this way, and takes 11–15 minutes per design.

How would you avoid redoing that work? Under what conditions would your approach give an answer close enough to a fresh drape, and when would it fail? How would you check, on a given garment, whether it worked?

Answer from your own knowledge only. Don't use any tools and don't read any files.
