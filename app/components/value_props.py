import reflex as rx


def value_prop_section(
    headline: str, body: str, bg_color: str = "bg-white", padding_y: str = "py-24"
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                headline,
                class_name="text-[28px] md:text-[32px] font-bold text-[#0F172A] mb-6 leading-tight",
            ),
            rx.el.p(
                body,
                class_name="text-[18px] md:text-[20px] text-[#64748B] leading-relaxed max-w-[700px]",
            ),
            class_name="max-w-5xl mx-auto px-6",
        ),
        class_name=f"{bg_color} {padding_y} w-full text-left",
    )


def value_props() -> rx.Component:
    return rx.fragment(
        value_prop_section(
            "Never miss a filing",
            "California biennial. Illinois annual. We watch the calendar so $250 late penalties, loss of good standing, and administrative dissolution never happen. Email reminders 30 days before each deadline.",
            bg_color="bg-white",
            padding_y="pt-32 pb-16 md:pt-40 md:pb-32",
        ),
        value_prop_section(
            "File in 2 minutes, not 2 hours",
            "Once you've added an LLC, each filing pre-fills from last cycle's data. Review, authorize, done. We submit to the state portal on your behalf — the same legal model LegalZoom and ZenBusiness use.",
            bg_color="bg-[#F8FAFC]",
            padding_y="py-16 md:py-32",
        ),
        value_prop_section(
            "Built for multi-LLC owners",
            "3–20 LLCs? One subscription at $19.99/year flat covers all of them. State filing fees are passed through at cost — no hidden markups, no per-LLC gouging.",
            bg_color="bg-white",
            padding_y="py-16 md:py-40",
        ),
    )