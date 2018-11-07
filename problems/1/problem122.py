"""Solution to problem 122 on project euler"""
# https://projecteuler.net/problem=122

# The most naive way of computing n15 requires fourteen multiplications:
# n � n � ... � n = n15
# But using a "binary" method you can compute it in six multiplications:
# n � n = n2n2 � n2 = n4n4 � n4 = n8n8 � n4 = n12n12 � n2 = n14n14 � n = n15
# However it is yet possible to compute it in only five multiplications:
# n � n = n2n2 � n = n3n3 � n3 = n6n6 � n6 = n12n12 � n3 = n15
# We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.


# Initial issue loading problem, likely graphic on site