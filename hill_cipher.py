import numpy as np

def matrix_mod_inv(matrix, modulus):
    det = int(np.linalg.det(matrix))
    det_inv = pow(det, -1, modulus)
    adjugate = (det_inv * np.linalg.inv(matrix).T * det) % modulus
    return adjugate.astype(int)

def encrypt(plaintext, key):
    # Implement Hill Cipher encryption
    # ...

def decrypt(ciphertext, key):
    # Implement Hill Cipher decryption
    # ...

# Contoh penggunaan:
# key_matrix = np.array([[2, 4, 5], [9, 2, 1], [3, 17, 7]])
# encrypted_text = encrypt("HELLO", key_matrix)
# decrypted_text = decrypt(encrypted_text, key_matrix)