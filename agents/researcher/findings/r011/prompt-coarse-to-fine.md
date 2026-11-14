I run a cloth-simulation pipeline in Blender (its built-in CPU cloth solver) that drapes garments on 3D figures. Each garment piece is about 5,000 vertices, and one drape takes about 4–7 minutes. What the pipeline judges a drape on is mostly its large-scale shape: the silhouette against a photo and landmark lengths (hem height, sleeve length). It also measures how much folding the cloth shows, and it requires that no cloth passes through the body or through other cloth.

How would you make each drape cheaper without changing what is measured? Under what conditions would your approach give the same answer as the full drape, and when would it fail? How would you check, on a given garment, whether it worked?

Answer from your own knowledge only. Don't use any tools and don't read any files.
