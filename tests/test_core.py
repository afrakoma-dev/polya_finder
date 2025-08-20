from polya_finder.core import find_motifs

def test_find_motifs():
    seq = "GGCAATAAAGGGAATAAATTT"
    expected = [3,12]
    assert find_motifs(seq) == expected