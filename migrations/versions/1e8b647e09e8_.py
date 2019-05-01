"""empty message

Revision ID: 1e8b647e09e8
Revises: 
Create Date: 2019-05-01 15:55:02.390144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e8b647e09e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=254), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('timeCreated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('timeModified', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('timeLastLogin', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Thread',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('timeCreated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('timeModified', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified', sa.Boolean(), server_default='false', nullable=True),
    sa.Column('locked', sa.Boolean(), server_default='false', nullable=True),
    sa.Column('accountId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['accountId'], ['Account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('threadId', sa.Integer(), nullable=True),
    sa.Column('parentCommentId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parentCommentId'], ['Comment.id'], ),
    sa.ForeignKeyConstraint(['threadId'], ['Thread.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Comment')
    op.drop_table('Thread')
    op.drop_table('Account')
    # ### end Alembic commands ###
