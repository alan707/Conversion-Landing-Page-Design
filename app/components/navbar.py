import reflex as rx
from app.states.landing_state import LandingState


def nav_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        label,
        href=href,
        class_name="text-sm font-medium text-gray-600 hover:text-indigo-600 transition-colors duration-200",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("layers", class_name="h-6 w-6 text-indigo-600"),
                        rx.el.span(
                            "Nexus",
                            class_name="text-xl font-bold tracking-tight text-gray-900",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    href="/",
                ),
                rx.el.div(
                    nav_link("Features", "#features"),
                    nav_link("Pricing", "#pricing"),
                    nav_link("About", "#"),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.div(
                    rx.el.a(
                        "Log In",
                        href="#",
                        class_name="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors",
                    ),
                    rx.el.a(
                        rx.el.button(
                            "Sign Up",
                            class_name="px-4 py-2 bg-gradient-to-r from-indigo-600 to-violet-600 text-white text-sm font-semibold rounded-lg hover:shadow-lg active:scale-[0.98] transition-all duration-200",
                        ),
                        href="#",
                    ),
                    class_name="hidden md:flex items-center gap-6",
                ),
                rx.el.button(
                    rx.cond(
                        LandingState.is_menu_open,
                        rx.icon("x", class_name="h-6 w-6"),
                        rx.icon("menu", class_name="h-6 w-6"),
                    ),
                    on_click=LandingState.toggle_menu,
                    class_name="md:hidden p-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between",
            ),
            rx.cond(
                LandingState.is_menu_open,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            nav_link("Features", "#features"),
                            nav_link("Pricing", "#pricing"),
                            nav_link("About", "#"),
                            class_name="flex flex-col gap-4 p-4 border-b border-gray-100",
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Log In",
                                href="#",
                                class_name="block w-full text-center py-2 text-sm font-medium text-gray-600",
                            ),
                            rx.el.button(
                                "Sign Up",
                                class_name="w-full py-2 bg-gradient-to-r from-indigo-600 to-violet-600 text-white text-sm font-semibold rounded-lg",
                            ),
                            class_name="p-4 flex flex-col gap-3",
                        ),
                        class_name="md:hidden bg-white border-b border-gray-200 shadow-xl animate-in fade-in slide-in-from-top-4 duration-200",
                    ),
                    class_name="absolute top-16 left-0 w-full z-40",
                ),
            ),
            class_name="relative",
        ),
        class_name="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-gray-200/50",
    )