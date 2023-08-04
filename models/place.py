#!/usr/bin/python3
"""This is the place class
"""
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship

association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Ceci est la classe pour Place
    Attributs:
        city_id: identifiant de la ville
        user_id: identifiant de l'utilisateur
        name: nom de la place
        description: description sous forme de chaîne
        number_rooms: nombre de chambres en entier (par défaut 0)
        number_bathrooms: nombre de salles de bain en entier (par défaut 0)
        max_guest: nombre maximum d'invités en entier (par défaut 0)
        price_by_night: prix pour une nuitée en entier (par défaut 0)
        latitude: latitude en flottant
        longitude: longitude en flottant
        reviews: relation avec les critiques (relie à la classe "Review")
        amenities: relation avec les commodités (relie à la classe "Amenity")
        amenity_ids: liste des identifiants d'amenities
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Obtenir une liste de toutes les critiques.
            """
            all_reviews = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    all_reviews.append(review)
            return all_reviews

        @property
        def amenities(self):
            """Obtenir les commodités liées.
            """
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Définir les commodités.
            """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)