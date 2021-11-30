def almostIncreasingSequence(sequence):
    if len(sequence) == 2:
        return True
        
    def is_increasing(seq):
        for i in range(len(seq) - 1):
            if seq[i] >= seq[i + 1]:
                return False
        return True
        
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            increasing = is_increasing(sequence[:i] + sequence[i+1:]) or is_increasing(sequence[:i+1] + sequence[i+2:])
            if not increasing:
                return False
    return True
