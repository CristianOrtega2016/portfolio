import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin
from reflex_components_radix.plugin import RadixThemesPlugin

config = rx.Config(
    app_name="Porfolio",
    env=rx.Env.DEV,
    plugins=[
        SitemapPlugin(),
        RadixThemesPlugin(),
    ],
)