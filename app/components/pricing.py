import reflex as rx


def pricing_card(
    title: str, price: str, description: str, is_solid: bool = False
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(title, class_name="text-[22px] font-bold text-[#0F172A] mb-2"),
            rx.el.div(
                rx.el.span(price, class_name="text-[28px] font-bold text-[#0F172A]"),
                class_name="mb-6",
            ),
            rx.el.p(
                description,
                class_name="text-[18px] text-[#64748B] mb-10 leading-relaxed min-h-[120px] flex-1",
            ),
            rx.el.a(
                rx.el.button(
                    "Get started",
                    class_name=rx.cond(
                        is_solid,
                        "w-full min-h-[56px] py-4 bg-[#0B5FFF] text-white font-bold rounded-[4px] hover:opacity-90 transition-all",
                        "w-full min-h-[56px] py-4 bg-white text-[#0F172A] font-bold border border-[#E2E8F0] rounded-[4px] hover:bg-[#F8FAFC] transition-all",
                    ),
                ),
                href="/signin",
                class_name="w-full mt-auto",
            ),
            class_name="p-8 h-full flex flex-col",
        ),
        class_name="bg-white border border-[#E2E8F0] rounded-[4px] flex flex-col h-full transition-all hover:border-[#0B5FFF]/30",
    )


def pricing_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Pricing",
                class_name="text-[28px] md:text-[32px] font-bold text-[#0F172A] mb-12",
            ),
            rx.el.div(
                pricing_card(
                    "1 LLC",
                    "Free",
                    "Add one LLC. We handle its filings for as long as you want, no credit card required.",
                    is_solid=False,
                ),
                pricing_card(
                    "2–10 LLCs",
                    "$19.99/year",
                    "Flat annual fee, regardless of how many LLCs (up to 10).",
                    is_solid=True,
                ),
                pricing_card(
                    "11+ LLCs",
                    "$49/year",
                    "For investors with larger portfolios.",
                    is_solid=False,
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
            ),
            rx.el.p(
                "State filing fees charged separately when each filing is submitted — $20 for California Statement of Information, $75 for Illinois Annual Report. No markup.",
                class_name="text-[15px] text-[#64748B] text-left mt-12",
            ),
            class_name="max-w-5xl mx-auto px-6 py-24 md:py-32",
        ),
        id="pricing",
        class_name="bg-[#F8FAFC]",
    )