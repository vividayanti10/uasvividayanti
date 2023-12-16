from flask import Flask, render_template, request
from hill_cipher import encrypt, decrypt

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    plaintext = request.form['plaintext']
    key_matrix = request.form['key_matrix']
    # Parsing key_matrix dari input dan panggil fungsi encrypt
    encrypted_text = encrypt(plaintext, key_matrix)
    return render_template('result.html', result=encrypted_text, operation='Encrypted')

@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    ciphertext = request.form['ciphertext']
    key_matrix = request.form['key_matrix']
    # Parsing key_matrix dari input dan panggil fungsi decrypt
    decrypted_text = decrypt(ciphertext, key_matrix)
    return render_template('result.html', result=decrypted_text, operation='Decrypted')

if _name_ == '_main_':
    app.run(debug=True)