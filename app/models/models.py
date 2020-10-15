from app import app

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(90))
    nome_de_usuario = db.Column(db.String(90), unique=True)
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String(20))

    def __init__(self, nome, nome_de_usuario, email, senha):
        self.nome = nome
        self.nome_de_usuario = nome_de_usuario
        self.email = email
        self.senha = senha

    def __repr__(self):
        return '<Usuario>'.format(self.nome_de_usuario)

class Publicacao(db.Model):
    __tablename__ = 'publicacoes'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    corpo = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    usuario = db.relationship('Usuario', foreign_keys=usuario_id)

    def __init__(self, titulo, corpo, usuario_id):
        self.titulo = titulo
        self.corpo = corpo
        self.usuario_id = usuario_id

    def __repr__(self):
        return "<Publicacao>".format(self.titulo)
