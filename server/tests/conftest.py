import pytest
import sqlalchemy as sa
from devtools.database import DatabaseAdapter, DatabaseConfig, Driver


@pytest.fixture
def database_adapter():
    adapter = DatabaseAdapter(
        DatabaseConfig(
            driver=Driver.SQLITE,
            host="/:memory:",
            pool_size=10,
            pool_recycle=3600,
            max_overflow=0,
            autotransaction=False,
        )
    )
    with adapter.context() as conn:
        conn.execute(
            sa.text(
                """
                CREATE TABLE zaw (
                    id uuid NOT NULL,
                    "name" text NULL,
                    created_at timestamp NOT NULL,
                    updated_at timestamp NULL,
                    "level" text NULL,
                    gild bool NULL,
                    link_id uuid NULL,
                    grip_id uuid NULL,
                    strike_id uuid NULL,
                    CONSTRAINT zaw_pkey PRIMARY KEY (id),
                    CONSTRAINT zaw_grip_id_fkey FOREIGN KEY (grip_id) REFERENCES zawgrip(id),
                    CONSTRAINT zaw_link_id_fkey FOREIGN KEY (link_id) REFERENCES zawlink(id),
                    CONSTRAINT zaw_strike_id_fkey FOREIGN KEY (strike_id) REFERENCES zawstrike(id)
                );
                """
            )
        )
        conn.execute(
            sa.text(
                """
                CREATE TABLE zawlink (
                    id uuid NOT NULL,
                    img_url text NULL,
                    "name" text NULL,
                    created_at timestamp NOT NULL,
                    updated_at timestamp NULL,
                    speed_bonus text NULL,
                    critical_chance text NULL,
                    status_chance text NULL,
                    damage_bonus text NULL,
                    CONSTRAINT zawlink_pkey PRIMARY KEY (id)
                );
                """
            )
        )
        conn.execute(
            sa.text(
                """
                CREATE TABLE zawstrike (
                    id uuid NOT NULL,
                    img_url text NULL,
                    "name" text NULL,
                    created_at timestamp NOT NULL,
                    updated_at timestamp NULL,
                    type_1h text NULL,
                    type_2h text NULL,
                    base_damage float8 NULL,
                    speed text NULL,
                    critical_chance text NULL,
                    critical_multiplier float8 NULL,
                    status text NULL,
                    riven_disposition float8 NULL,
                    impact_damage float8 NULL,
                    puncture_damage float8 NULL,
                    slash_damage float8 NULL,
                    viral_damage float8 NULL,
                    CONSTRAINT zawstrike_pkey PRIMARY KEY (id)
                );
                """
            )
        )
        conn.execute(
            sa.text(
                """
                CREATE TABLE zawgrip (
                    id uuid NOT NULL,
                    img_url text NULL,
                    "name" text NULL,
                    created_at timestamp NOT NULL,
                    updated_at timestamp NULL,
                    grip_type text NULL,
                    damage_bonus text NULL,
                    base_speed float8 NULL,
                    CONSTRAINT zawgrip_pkey PRIMARY KEY (id)
                );
                """
            )
        )
        conn.commit()
    return adapter
