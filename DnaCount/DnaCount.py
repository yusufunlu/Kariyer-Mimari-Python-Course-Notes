DNA = input("Enter Dna Sequence")
A = DNA.count("A")
T = DNA.count("T")
C = DNA.count("C")
G = DNA.count("G")

print("number of A in your sequence is ",A)
print("number of T in your sequence is ",T)
print("number of C in your sequence is ",C)
print("number of G in your sequence is ",G)

print("GC ratio is ", (G+C)/(G+C+T+A))
