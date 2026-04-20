import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p("© 2026 LLC Keeper", class_name="text-[15px] text-[#64748B]"),
                rx.el.div(
                    rx.el.a(
                        "alan@llckeeper.com",
                        href="mailto:alan@llckeeper.com",
                        class_name="text-[15px] text-[#64748B] hover:text-[#0B5FFF]",
                    ),
                    rx.el.span(" · ", class_name="text-[#64748B]"),
                    rx.el.a(
                        "Privacy",
                        href="#",
                        class_name="text-[15px] text-[#64748B] hover:text-[#0B5FFF]",
                    ),
                    rx.el.span(" · ", class_name="text-[#64748B]"),
                    rx.el.a(
                        "Terms",
                        href="#",
                        class_name="text-[15px] text-[#64748B] hover:text-[#0B5FFF]",
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="flex flex-col md:flex-row justify-between items-center gap-4 text-center md:text-left",
            ),
            class_name="max-w-5xl mx-auto px-6 py-8",
        ),
        class_name="bg-white border-t border-[#E2E8F0]",
    )