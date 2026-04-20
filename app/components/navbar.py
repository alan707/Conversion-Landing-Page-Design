import reflex as rx
from app.states.landing_state import LandingState


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "LLC Keeper",
                    href="/",
                    class_name="text-xl font-bold tracking-tight text-[#0F172A]",
                ),
                rx.el.div(
                    rx.el.a(
                        "Pricing",
                        href="#pricing",
                        class_name="text-lg font-medium text-[#64748B] hover:text-[#0B5FFF] transition-colors",
                    ),
                    rx.el.a(
                        rx.el.button(
                            "Sign in",
                            class_name="px-6 py-2.5 bg-[#0B5FFF] text-white text-lg font-semibold rounded-[4px] hover:opacity-90 active:scale-[0.98] transition-all",
                        ),
                        href="/signin",
                    ),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.button(
                    rx.cond(
                        LandingState.is_menu_open,
                        rx.icon("x", class_name="h-6 w-6 text-[#0F172A]"),
                        rx.icon("menu", class_name="h-6 w-6 text-[#0F172A]"),
                    ),
                    on_click=LandingState.toggle_menu,
                    class_name="md:hidden p-2 min-h-[44px] min-w-[44px] flex items-center justify-center hover:bg-[#F8FAFC] rounded-[4px] transition-colors",
                ),
                class_name="max-w-5xl mx-auto px-6 h-20 flex items-center justify-between",
            ),
            rx.cond(
                LandingState.is_menu_open,
                rx.el.div(
                    rx.el.div(
                        rx.el.a(
                            "Pricing",
                            href="#pricing",
                            on_click=LandingState.close_menu,
                            class_name="block px-6 py-4 text-lg font-medium text-[#64748B] border-b border-[#E2E8F0]",
                        ),
                        rx.el.div(
                            rx.el.a(
                                rx.el.button(
                                    "Sign in",
                                    class_name="w-full py-3 bg-[#0B5FFF] text-white font-bold rounded-[4px]",
                                ),
                                href="/signin",
                                on_click=LandingState.close_menu,
                            ),
                            class_name="p-6",
                        ),
                        class_name="md:hidden bg-white border-b border-[#E2E8F0] shadow-xl",
                    ),
                    class_name="absolute top-20 left-0 w-full z-40",
                ),
            ),
            class_name="relative",
        ),
        class_name="fixed top-0 w-full z-50 bg-white border-b border-[#E2E8F0]",
    )