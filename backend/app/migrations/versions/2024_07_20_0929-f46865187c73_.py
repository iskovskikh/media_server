"""empty message

Revision ID: f46865187c73
Revises: 
Create Date: 2024-07-20 09:29:25.539592

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'f46865187c73'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    user_table = op.create_table(
        'users',
        sa.Column('oid', sa.String(), nullable=False),
        sa.Column('login', sa.String(), nullable=False),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('company', sa.String(), nullable=False),
        sa.Column('position', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('oid')
    )
    # ### end Alembic commands ###

    op.bulk_insert(
        user_table,
        [
            dict(
                login='user1',
                full_name='Энтони Кидис',
                password='user1',
                company='RHCP',
                position='вокалист',
                oid='6391be0e-3245-4737-a64f-b8e89159f799'
            ),
            dict(
                login='user2',
                full_name='Майкл Питер Бэлзари',
                password='user2',
                company='RHCP',
                position='бас-гитарист',
                oid='c6e07610-6e7d-4f94-ae68-a755a421803c'
            ),
            dict(
                login='user3',
                full_name='Чэд Смит',
                password='user3',
                company='RHCP',
                position='ударник',
                oid='02403500-a060-41cd-b2ba-f94bff2111e8'
            ),
            dict(
                login='user4',
                full_name='Джон Фрушанте',
                password='user4',
                company='RHCP',
                position='гитарист',
                oid='a8bccf81-d473-4d57-8c62-912593770474'
            ),
        ],
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
