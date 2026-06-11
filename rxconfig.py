import reflex as rx

config = rx.Config(
    app_name="Porfolio",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    frontend_packages=[
        "react",
        "react-dom"
    ]
)