import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.features import features_section
from app.components.pricing import pricing_section
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero(),
        features_section(),
        pricing_section(),
        footer(),
        class_name="min-h-screen bg-white font-['Inter'] selection:bg-indigo-100 selection:text-indigo-900",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")