I run a cloth-simulation pipeline in Blender (its built-in CPU cloth solver) that fits a garment's sewing pattern to a photo. Each garment piece is about 5,000 vertices. A fitting loop changes the cut (lengths and widths of the pattern pieces) and drapes the garment again to see the effect. It drapes once at the starting cut; once per group of controls, moving each control 3–8 cm, to estimate how each measured landmark (hem height, sleeve length and so on) responds; and then once per step of a damped least-squares solve, at most 3 steps.

Every drape starts from the flat pattern: the pieces are placed around the body, the seams are closed, and the cloth falls and settles under gravity. One drape takes about 4–7 minutes, and the whole loop 27–35 minutes.

How would you avoid redoing that work? Under what conditions would your approach give the same answer as draping from scratch, and when would it fail? How would you check, on a given garment, whether it worked?

Answer from your own knowledge only. Don't use any tools and don't read any files.
