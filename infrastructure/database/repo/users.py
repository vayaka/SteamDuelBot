from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models.users import User
from infrastructure.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def get_or_create_user(
            self,
            user_id: int,
            full_name: str,
            username: Optional[str] = None,
            steam_id: Optional[int] = None,
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param user_id: The user's ID.
        :param full_name: The user's full name.
        :param username: The user's username. It's an optional parameter.
        :param steam_id: The user's Steam ID. It's an optional parameter.
        :return: User object, None if there was an error while making a transaction.
        """

        insert_stmt = (
            insert(User).values(
                user_id=user_id,
                username=username,
                full_name=full_name,
                steam_id=steam_id,
            ).on_conflict_do_update(
                index_elements=[User.user_id],
                set_=dict(
                    username=username,
                    full_name=full_name,
                    steam_id=steam_id,
                ),
            ).returning(User)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one()
    # async def update_user(self,
    #                       user_id: int,
    #                       steam_id: int,
    #                       username: str,
    #                       full_name: str):
    #     """
    #     Updates a user's Steam ID.
    #     :param full_name: The user's full name.
    #     :param username: The user's username.
    #     :param user_id: The user's ID.
    #     :param steam_id: The user's Steam ID.
    #     :return: None
    #     """
    #     update_stmt = (
    #         update(User).where(User.user_id == user_id).values(steam_id=steam_id, username=username, full_name=full_name)
    #     )
    #     await self.session.execute(update_stmt)
    #     await self.session.commit()
