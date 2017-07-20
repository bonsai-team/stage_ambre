# AIDE

### filtre_aln.py
`python filtre_aln.py aln.sam`
Script qui retire les alignements qui prennent en compte moins de x% du read en compte. (x à changer dans le script)

### error_rate.py
`python error_rate.py aln.sam`
Script qui crée un fichier aln_error_rate.txt, avec un taux d'erreur par ligne. A faire tourner sur un fichier nettoyé des reads superflus avec filtre_aln.py

### couverture.py
`python couverture.py aln.sam`

Script qui affiche le nombre de transcrits touchés par au moins un alignement (couverture verticale) et qui crée deux fichiers (couverture horizontale): 
<li>aln_tot.txt : recense la couverture horizontale par transcrit en prenant en compte tous les reads
<li>aln_read.txt : recense la couverture horizontale par transcrit en prenant en compte le read le plus long

### sam2sortedbam.sh
`sh sam2sortedbam.sh aln.sam reference.fasta`
Réalise dans l'ordre les scripts ci dessus sur un fichier sam. Les fichiers de sorties sont :
<li> new_aln.sam : fichier sam avec certains alignements retirés
<li> new_aln.bam
<li> new_aln_sorted.bam
<li> new_aln_sorted.bai
