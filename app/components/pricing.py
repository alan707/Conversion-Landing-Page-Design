import reflex as rx


def pricing_card(
    title: str, price: str, features: list[str], is_popular: bool = False
) -> rx.Component:
    return rx.el.div(
        rx.cond(
            is_popular,
            rx.el.div(
                "Most Popular",
                class_name="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 bg-indigo-600 text-white text-xs font-bold rounded-full uppercase tracking-wider",
            ),
        ),
        rx.el.div(
            rx.el.h3(title, class_name="text-xl font-bold text-gray-900 mb-2"),
            rx.el.div(
                rx.el.span(
                    f"${price}", class_name="text-4xl font-extrabold text-gray-900"
                ),
                rx.el.span("/mo", class_name="text-gray-500 ml-1 font-medium"),
                class_name="mb-6",
            ),
            rx.el.ul(
                rx.foreach(
                    features,
                    lambda f: rx.el.li(
                        rx.icon(
                            "check", class_name="h-4 w-4 text-emerald-500 shrink-0"
                        ),
                        rx.el.span(f, class_name="text-sm text-gray-600"),
                        class_name="flex items-center gap-3",
                    ),
                ),
                class_name="space-y-4 mb-8",
            ),
            rx.el.button(
                "Choose Plan",
                class_name=rx.cond(
                    is_popular,
                    "w-full py-3 bg-indigo-600 text-white font-bold rounded-xl shadow-lg hover:bg-indigo-700 transition-all active:scale-[0.98]",
                    "w-full py-3 bg-gray-50 text-gray-900 font-bold border border-gray-200 rounded-xl hover:bg-gray-100 transition-all active:scale-[0.98]",
                ),
            ),
            class_name="p-8 h-full flex flex-col",
        ),
        class_name=rx.cond(
            is_popular,
            "relative bg-white border-2 border-indigo-600 rounded-3xl shadow-xl scale-105 z-10",
            "bg-white border border-gray-200 rounded-3xl shadow-sm",
        ),
    )


def pricing_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Simple, transparent pricing",
                    class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-4 text-center",
                ),
                rx.el.p(
                    "Choose the plan that's right for your business scale.",
                    class_name="text-gray-600 text-center max-w-2xl mx-auto mb-16",
                ),
            ),
            rx.el.div(
                pricing_card(
                    "Free",
                    "0",
                    [
                        "Up to 3 accounts",
                        "Basic analytics",
                        "Community support",
                        "Public API access",
                    ],
                ),
                pricing_card(
                    "Pro",
                    "49",
                    [
                        "Unlimited accounts",
                        "Advanced insights",
                        "Priority 24/7 support",
                        "Custom integrations",
                        "Team collaboration",
                    ],
                    is_popular=True,
                ),
                pricing_card(
                    "Enterprise",
                    "199",
                    [
                        "Dedicated account manager",
                        "Custom SLA",
                        "Security auditing",
                        "Private cloud deployment",
                        "Bulk data export",
                    ],
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8 items-center max-w-6xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24",
        ),
        id="pricing",
        class_name="bg-gray-50/50",
    )