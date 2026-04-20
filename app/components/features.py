import reflex as rx


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-indigo-600"),
            class_name="size-12 rounded-xl bg-indigo-50 flex items-center justify-center mb-6 group-hover:bg-indigo-600 group-hover:text-white transition-colors duration-300",
        ),
        rx.el.h3(title, class_name="text-xl font-bold text-gray-900 mb-3"),
        rx.el.p(description, class_name="text-gray-600 leading-relaxed text-sm"),
        class_name="group p-8 bg-white border border-gray-100 rounded-2xl shadow-sm hover:shadow-md hover:-translate-y-1 transition-all duration-300",
    )


def features_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Engineered for growth",
                    class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-4 text-center",
                ),
                rx.el.p(
                    "Everything you need to scale your operations securely.",
                    class_name="text-gray-600 text-center max-w-2xl mx-auto mb-16",
                ),
            ),
            rx.el.div(
                feature_card(
                    "shield",
                    "Advanced Security",
                    "Enterprise-grade encryption and multi-factor authentication for every single account interaction.",
                ),
                feature_card(
                    "bar-chart-3",
                    "Real-time Analytics",
                    "Gain deep insights into your resource usage with automated reporting and custom dashboard views.",
                ),
                feature_card(
                    "zap",
                    "Easy Integration",
                    "Connect your existing stack in minutes with our robust API and pre-built connector ecosystem.",
                ),
                feature_card(
                    "headset",
                    "24/7 Priority Support",
                    "Our dedicated engineering team is available around the clock to help you optimize your workflow.",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24",
        ),
        id="features",
        class_name="bg-white",
    )