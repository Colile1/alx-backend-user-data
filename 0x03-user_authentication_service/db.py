#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """
    DB class
    """
    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find the first user matching the given criteria
        or raise appropriate errors.
        If no user is found, raise NoResultFound.
        If the query is invalid, raise InvalidRequestError.
        """
        from sqlalchemy.orm.exc import NoResultFound
        from sqlalchemy.exc import InvalidRequestError
        session = self._session
        try:
            query = session.query(User).filter_by(**kwargs)
            user = query.one()
            return user
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes and commit changes.
        Raise ValueError if attribute is invalid.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"User has no attribute '{key}'")
            setattr(user, key, value)
        self._session.commit()

    def find_user_by_id(self, user_id: int) -> User:
        """Find a user by their ID or raise a ValueError if not found."""
        user = self._session.query(User).filter_by(id=user_id).first()
        if not user:
            raise ValueError(
                f"User with id = {user_id} not found"
            )
        return user

    def find_user_by_email(self, email: str) -> User:
        """Find a user by their email or raise a ValueError if not found."""
        user = self._session.query(User).filter_by(email=email).first()
        if not user:
            raise ValueError(
                f"User with email = {email} not found"
            )
        return user

    def find_user_by_reset_token(self, reset_token: str) -> User:
        """
        Find a user by their reset token or raise a ValueError if not found.
        If reset_token is None, return None.
        """
        query = self._session.query(User)
        filtered_query = query.filter_by(reset_token=reset_token)
        user = filtered_query.first()

        if not user:
            raise ValueError(
                f"User with reset_token = {reset_token} not found"
            )
        return user

    def find_user_by_session_id(self, session_id: str) -> User:
        """
        Find a user by their session ID or raise a ValueError if not found.
        If session_id is None, return None.
        """
        query = self._session.query(User)
        filtered_query = query.filter_by(session_id=session_id)
        user = filtered_query.first()

        if not user:
            raise ValueError(
                f"User with session_id = {session_id} not found"
            )
        return user

    def is_email_registered(self, email: str) -> bool:
        """Check if an email is already registered in the system."""
        user = self._session.query(User).filter_by(email=email).first()
        return user is not None

    def register_user(self, email: str, hashed_password: str) -> User:
        """Register a new user with the given email and password."""
        if self.is_email_registered(email):
            raise ValueError(
                f"User with email = {email} already registered"
            )
        return self.add_user(email, hashed_password)
