import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin
from reflex_components_radix.plugin import RadixThemesPlugin

config = rx.Config(
    app_name="Porfolio",
    env=rx.Env.DEV,
    plugins=[
        SitemapPlugin(),
        # Force the dark theme on every device so phones (usually light mode)
        # match the desktop/dark color scheme the author sees.
        RadixThemesPlugin(theme=rx.theme(color_mode="dark")),
    ],
)