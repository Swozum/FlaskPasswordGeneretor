from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField, SubmitField
from wtforms.validators import NumberRange, DataRequired
import string
import random
from itertools import product

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf_123'

class SenhaForm(FlaskForm):
    quantidade = IntegerField('Quantidade de senhas a serem geradas:', validators=[DataRequired(),NumberRange(min=1)])
    tamanho = IntegerField('Tamanho da senha:', validators=[DataRequired(),NumberRange(min=1)])
    uppercase = BooleanField('Incluir letras maiusculas')
    lowercase = BooleanField('Incluir letras minusculas')
    numbers = BooleanField('Incluir numeros')
    special_chars = BooleanField('Incluir caracteres especiais')
    similar = BooleanField('Evitar caracteres parecidos')
    repetida = BooleanField('Evitar caracteres repetidos')
    sequencial = BooleanField('Evitar caracteres sequenciais')
    submit = SubmitField('Gerar Senhas')

    
    
def generate_password(quantidade, length, uppercase, lowercase, numbers, special_chars, similar, repetida, sequencial):
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase.translate({ord(c): None for c in 'ILLO'})  # Remove caracteres similares
    if lowercase:
        chars += string.ascii_lowercase.translate({ord(c): None for c in 'illo'})  # Remove caracteres similares
    if numbers:
        chars += string.digits.translate({ord(c): None for c in '01'})
    if special_chars:
        chars += string.punctuation

    passwords = []
    while len(passwords) < quantidade:
        password = ''.join(random.choice(chars) for _ in range(length))

        if similar:
            password = password.translate({ord(c): None for c in 'ILLOillo'})  # Remove caracteres similares

        if repetida and len(set(password)) != len(password):
            continue

        if sequencial:
            sequential = False
            for i in range(len(password) - 2):
                if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
                    sequential = True
                    break

            if sequential:
                continue

        passwords.append(password)

    return passwords

def similarity_check(passwords):
    similar = set()
    for p1, p2 in product(passwords, repeat=2):
        if p1 != p2 and p1 in p2:
            similar.add(p2)
    return list(similar)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SenhaForm()

    if form.validate_on_submit():
        quantidade = form.quantidade.data
        tamanho = form.tamanho.data
        uppercase = form.uppercase.data
        lowercase = form.lowercase.data
        numbers = form.numbers.data
        special_chars = form.special_chars.data
        similar = form.similar.data
        repetida = form.repetida.data
        sequencial = form.sequencial.data

        # Verifica se pelo menos uma opção está marcada
        if not (uppercase or lowercase or numbers or special_chars):
            aviso = 'Selecione pelo menos uma das 4 primeiras opções para gerar senhas.'
            return render_template('index.html', form=form, aviso=aviso)

        generated_passwords = generate_password(quantidade, tamanho, uppercase, lowercase, numbers, special_chars, similar, repetida, sequencial)
        similar_passwords = similarity_check(generated_passwords)

        return render_template('index.html', form=form, passwords=generated_passwords, similar_passwords=similar_passwords)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=False)
