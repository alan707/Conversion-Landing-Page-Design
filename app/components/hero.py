import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Your LLC filings, filed in minutes.",
                    class_name="text-[32px] md:text-[48px] font-bold text-[#0F172A] mb-8 leading-tight",
                ),
                rx.el.p(
                    "Auto-prepared California Statement of Information and Illinois Annual Report filings. Never miss a deadline, never retype your entity info.",
                    class_name="text-[18px] md:text-[20px] text-[#64748B] mb-12 max-w-[700px] leading-relaxed",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.button(
                            "Get started — 1 LLC free",
                            class_name="w-full md:w-auto min-h-[56px] px-8 py-4 bg-[#0B5FFF] text-white font-bold rounded-[4px] hover:opacity-90 transition-all text-lg flex items-center justify-center",
                        ),
                        href="/signin",
                        class_name="w-full md:w-auto",
                    ),
                    rx.el.p(
                        "Built by a multi-LLC owner who got tired of paying lawyers for paperwork. No password to remember — we sign you in with a magic link.",
                        class_name="mt-6 text-[15px] text-[#64748B] max-w-[450px]",
                    ),
                    class_name="flex flex-col items-start",
                ),
                class_name="max-w-5xl mx-auto px-6",
            ),
            class_name="pt-32 pb-24 md:pt-44 md:pb-32",
        ),
        class_name="bg-[#F8FAFC] w-full",
    )