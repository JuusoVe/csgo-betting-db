from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(128), unique=False, nullable=False)
    first_name = db.Column(db.String(128), unique=False, nullable=True)
    last_name = db.Column(db.String(128), unique=False, nullable=True)

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

class Team (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    organization = db.Column(db.Integer, db.ForeignKey('organization.id'),
        nullable=False)
    player_1_id = db.Column(db.Integer, db.ForeignKey('player.id'),
        nullable=False)
    player_2_id = db.Column(db.Integer, db.ForeignKey('player.id'),
        nullable=False)
    player_3_id = db.Column(db.Integer, db.ForeignKey('player.id'),
        nullable=False)
    player_4_id = db.Column(db.Integer, db.ForeignKey('player.id'),
        nullable=False)
    player_5_id = db.Column(db.Integer, db.ForeignKey('player.id'),
        nullable=False)
    player_6_id = db.Column(db.Integer, db.ForeignKey('player.id'),
        nullable=True)