def find_motifs(seq: str, motif: str = "AATAAA") -> list:
    positions = []
    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i+len(motif)] == motif:
            positions.append(i)
    return positions
