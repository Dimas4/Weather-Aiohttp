import sqlalchemy as sa


meta = sa.MetaData()

location = sa.Table(
    'location', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('location_name', sa.String(200), nullable=False),

    sa.PrimaryKeyConstraint('id', name='location_id_pkey'))

weather = sa.Table(
    'weather', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('location_id', sa.Integer, nullable=False),
    sa.Column('temp', sa.Float, nullable=False),
    sa.Column('humidity', sa.Float, nullable=False),
    sa.Column('pressure', sa.Float, nullable=False),

    sa.PrimaryKeyConstraint('id', name='weather_id_pkey'),
    sa.ForeignKeyConstraint(['location_id'], [location.c.id],
                            name='weather_question_id_fkey',
                            ondelete='CASCADE'),
)
