import reflex as rx


def footer_col(title: str, links: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            title,
            class_name="text-sm font-bold text-gray-900 uppercase tracking-widest mb-6",
        ),
        rx.el.ul(
            rx.foreach(
                links,
                lambda link: rx.el.li(
                    rx.el.a(
                        link,
                        href="#",
                        class_name="text-sm text-gray-500 hover:text-indigo-600 transition-colors",
                    )
                ),
            ),
            class_name="space-y-4",
        ),
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("layers", class_name="h-6 w-6 text-indigo-600"),
                        rx.el.span(
                            "Nexus",
                            class_name="text-xl font-bold tracking-tight text-gray-900",
                        ),
                        class_name="flex items-center gap-2 mb-6",
                    ),
                    rx.el.p(
                        "Providing modern account management solutions for high-growth digital teams worldwide.",
                        class_name="text-sm text-gray-500 max-w-xs",
                    ),
                    class_name="col-span-1 md:col-span-2",
                ),
                footer_col(
                    "Product", ["Features", "Security", "Pricing", "Enterprise"]
                ),
                footer_col("Company", ["About Us", "Careers", "Blog", "News"]),
                footer_col(
                    "Legal", ["Privacy Policy", "Terms of Service", "Cookie Policy"]
                ),
                class_name="grid grid-cols-2 md:grid-cols-5 gap-12 mb-16",
            ),
            rx.el.div(
                rx.el.p(
                    f"© {rx.State.router.page.params.get('year', '2024')} Nexus Inc. All rights reserved.",
                    class_name="text-xs text-gray-400",
                ),
                rx.el.div(
                    rx.icon(
                        "twitter",
                        class_name="h-4 w-4 text-gray-400 hover:text-indigo-600 cursor-pointer",
                    ),
                    rx.icon(
                        "github",
                        class_name="h-4 w-4 text-gray-400 hover:text-indigo-600 cursor-pointer",
                    ),
                    rx.icon(
                        "linkedin",
                        class_name="h-4 w-4 text-gray-400 hover:text-indigo-600 cursor-pointer",
                    ),
                    class_name="flex gap-6",
                ),
                class_name="pt-8 border-t border-gray-100 flex flex-col md:flex-row justify-between items-center gap-4",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
        ),
        class_name="bg-white border-t border-gray-100",
    )