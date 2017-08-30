# AIDE

### compare_sam.py
`python compare_sam.py aln1.sam aln2.sam`
Script qui compare deux fichiers d'alignement au format SAM. 
En sortie, il donne le nombre d'alignements différents, le nombre d'alignements sur la même référence, le nombre d'alignements exacts en commun et le nombre d'alignements communs à 5000 bases près.

### comptage_reads.py
`python comptage_reads.py aln.sam`
Script qui compte le nombre de reads différents dans un fichier d'alignement au format SAM.

### comptage_transcrits.py
`python comptage_transcrits.py aln.sam`
Script qui compte le nombre de transcrits et de gènes différents touchés par un alignement dans un fichier au format SAM.

### correspondance_megablast.py
`python correspondance_megablast.py aln.sam`
Script qui donne les bons noms aux Query des alignements produits par Megablast.

### filtre_transcript.py
`python filtre_transcript.py reference.fa`
Script qui retire les séquences de taille inférieure à 200 nucléotides dans une référence transcriptomique.

### mean_evalue.py
`python mean_evalue.py aln.sam`
Script qui calcule la evalue minimum, maximum et moyenne dans un fichier d'alignement au format SAM.

### parse_identity.py
`python parse_identity.py aln.sam ID`
Script dont l'output est un nouveau fichier SAM qui ne contient pas les alignements dont le pourcentage d'identité est inférieur à ID.

### parse_sam.py
`python parse_sam.py aln.sam read_list.txt`
Script qui va extraire les alignements des lectures contenues dans le fichier read_list.txt.

### parse_size.py
`python parse_size.py aln.sam SIZE`
Script dont l'output est un nouveau fichier SAM qui ne contient pas les alignements dont la taille est inférieure à SIZE.

### qualite_graph.py
`python qualite_graph.py aln.sam edges_list.txt`
Vérifie que les edges d'un graphe met bien en relation deux lectures qui se mappent sur la même référence transcriptomique.

### reads_comparaison.py
`python reads_comparaison.py aln1.sam aln2.sam`
Script qui réalise l'intersection des lectures alignées entre deux fichiers d'alignement au format SAM.

### unmapped_reads.py
`python unmapped_reads.py aln.sam reads.fa`
Script qui extrait les lectures non alignées à partir d'un fichier d'alignement au format SAM.

### verif_composantes.py
`python verif_composantes.py liste_reads_genes verif_graph.txt`
Script qui compte le nombre de transcrits et de gènes touchés par un graphe crée avec le script "aln2gfa2". "liste_reads_genes" est un fichier qui contient sur chaque ligne : lecture gene transcrit, extrait du fichier d'alignement qui a servi à crée le graphe.
En sortie du script : le nombre de composantes du graphe, le nombre de composantes pertinentes...

### verif_graphe.py
`python verif_composantes.py verif_graph.txt aln.sam ref.fa chr`
verif_graph.txt : fichier qui recense les lectures par composantes et qui est un des output de "aln2gfa2".
aln.sam : le fichier d'alignement qui a servi a crée le graphe.
ref.fa : référence sur laquelle les lectures ont été alignées.
chr : le chromosome a partir duquel les lectures ont été isolées d'un fichier d'alignement.
En sortie du script : le nombre de composantes du graphe, le nombre de composantes pertinentes...
