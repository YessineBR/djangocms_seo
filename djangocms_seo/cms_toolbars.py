from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from django.utils.translation import gettext_lazy as _
from .models import SeoExtension
import logging

logger = logging.getLogger(__name__)


@toolbar_pool.register
class SeoToolbar(CMSToolbar):
    """Toolbar for managing SEO options."""

    def populate(self):
        # Ensure the user has the necessary permissions
        if not self.request.user.has_perm("cms.change_page"):
            logger.warning("User lacks cms.change_page permission.")
            return

        # Get the current CMS page
        page = self.request.current_page
        if not page:
            logger.warning("No current page found.")
            return

        # Create or get the SEO menu
        menu = self.toolbar.get_or_create_menu("seo-menu", _("SEO Options"))

        # Fetch the SEO extension for the page, if it exists
        seo_extension = self.get_seo_extension(page)

        # Add appropriate menu items based on whether an SEO extension exists
        if seo_extension:
            self.add_edit_menu_item(menu, seo_extension)
        else:
            self.add_add_menu_item(menu, page)

        # Add a link to the SEO overview
        self.add_overview_menu_item(menu)

    @staticmethod
    def get_seo_extension(page):
        """Fetch the SeoExtension for the given page."""
        try:
            return SeoExtension.objects.get(extended_object=page)
        except SeoExtension.DoesNotExist:
            logger.info(f"No SeoExtension found for page ID {page.pk}.")
            return None

    @staticmethod
    def add_edit_menu_item(menu, seo_extension):
        """Add the 'Edit SEO Settings' menu item."""
        url = admin_reverse(
            "djangocms_seo_seoextension_change", args=[seo_extension.pk]
        )
        menu.add_modal_item(_("Edit SEO Settings"), url=url)

    @staticmethod
    def add_add_menu_item(menu, page):
        """Add the 'Add SEO Settings' menu item."""
        url = admin_reverse("djangocms_seo_seoextension_add") + f"?extended_object={page.pk}"
        menu.add_modal_item(_("Add SEO Settings"), url=url)

    @staticmethod
    def add_overview_menu_item(menu):
        """Add the 'SEO Overview' menu item."""
        url = admin_reverse("djangocms_seo_seoextension_changelist")
        menu.add_sideframe_item(_("SEO Overview"), url=url)
