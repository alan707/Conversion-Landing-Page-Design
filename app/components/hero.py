import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "New: Version 2.0 is now live ✦",
                    class_name="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-indigo-50 text-indigo-700 border border-indigo-100 mb-8",
                ),
                rx.el.h1(
                    "Manage your accounts with absolute precision.",
                    class_name="text-5xl md:text-7xl font-extrabold tracking-tight text-gray-900 mb-6 leading-[1.1]",
                ),
                rx.el.p(
                    "Nexus provides the ultimate workspace for modern teams to manage, scale, and secure their digital infrastructure with a single intuitive interface.",
                    class_name="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto mb-10 leading-relaxed",
                ),
                rx.el.div(
                    rx.el.button(
                        "Get Started Free",
                        class_name="px-8 py-4 bg-gradient-to-r from-indigo-600 to-violet-600 text-white font-bold rounded-xl shadow-lg hover:shadow-indigo-200 hover:scale-[1.02] active:scale-[0.98] transition-all duration-300",
                    ),
                    rx.el.button(
                        "Log In to Dashboard",
                        class_name="px-8 py-4 bg-white text-gray-700 font-bold border border-gray-200 rounded-xl shadow-sm hover:bg-gray-50 hover:border-gray-300 active:scale-[0.98] transition-all duration-300",
                    ),
                    class_name="flex flex-col sm:flex-row items-center justify-center gap-4",
                ),
                class_name="text-center max-w-4xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 md:py-32",
        ),
        class_name="relative bg-gradient-to-b from-indigo-50/50 to-white pt-16 overflow-hidden",
    )