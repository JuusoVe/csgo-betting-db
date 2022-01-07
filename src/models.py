from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=False, nullable=False)
    first_name = db.Column(db.String(64), unique=False, nullable=True)
    last_name = db.Column(db.String(64), unique=False, nullable=True)
    nick_first_last = db.Column(db.String(128), unique=True, nullable=False)
    hltv_id = db.Column(db.Integer, unique=True, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class Team (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
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
    coach = db.Column(db.Integer, db.ForeignKey('player.id'),
                      nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lan = db.Column(db.Boolean, nullable=True)
    team_1_id = db.Column(db.Integer, db.ForeignKey('team.id'),
                          nullable=False)
    team_2_id = db.Column(db.Integer, db.ForeignKey('team.id'),
                          nullable=False)
    format = db.Column(db.String(3), unique=False, nullable=True)
    map_1 = db.Column(db.String(64), unique=False, nullable=True)
    map_2 = db.Column(db.String(64), unique=False, nullable=True)
    map_3 = db.Column(db.String(64), unique=False, nullable=True)
    map_4 = db.Column(db.String(64), unique=False, nullable=True)
    map_5 = db.Column(db.String(64), unique=False, nullable=True)
    map_1_winner = db.Column(db.Integer, nullable=True)
    map_2_winner = db.Column(db.Integer, nullable=True)
    map_3_winner = db.Column(db.Integer, nullable=True)
    map_4_winner = db.Column(db.Integer, nullable=True)
    map_5_winner = db.Column(db.Integer, nullable=True)
    match_winner = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
