
from Bio.Seq import Seq



seq1 = Seq("ACTGACGTTACGTCAGTGGCTAACGT") 
print ( " coding strand is: :", seq1)


seq2 = seq1.complement()
print (" template strand is :", seq2)

seq2_reverse = seq2 [::-1]
print (" reverse template strand is : " , seq2_reverse) 

RNA1 = seq1.replace("T", "U")
print ("RNA is :", RNA1) 
RNA2 = seq1.transcribe()
print ("RNA is :", RNA2)

protein = seq1.translate()
print (" protein is :", protein)

print (len(seq1))

x = 31059/12

seq3 = Seq("ATGCGTACGTAGCTAGCTAGCTAGC")
percentage_T = seq3.count ("T") / len (seq3) *100
print (percentage_T)

RNA3 = seq3.replace ("T", "U")
print ( RNA3) 

seq4 = seq3.complement()
print (seq4) 

RNA3 = seq3.transcribe()
print (RNA3) 

seq4_reverse = seq4 [::-1]
print (seq4_reverse) 

protein2 = seq3.translate()
print (protein2)  

combined = protein2 + seq4
print (combined)

RNA3_reverse = RNA3[::-1]
print (RNA3_reverse)

seq6 = Seq("ATATAGCGATGC")

Coding = seq6.complement()
print (Coding)






