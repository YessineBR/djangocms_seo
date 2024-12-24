from django import forms

from .models import SeoExtension


class MetaTagInlineForm(forms.ModelForm):
    class Meta:
        model = SeoExtension.meta_tags.through
        fields = "__all__"

    def __str__(self):
        # Ensures the display uses the __str__ of the related MetaTag model
        return str(self.instance.metatag)


class OpenGraphMetaTagInlineForm(forms.ModelForm):
    class Meta:
        model = SeoExtension.og_meta.through
        fields = "__all__"

    def __str__(self):
        return str(self.instance.opengraphmeta)


class TwitterMetaTagInlineForm(forms.ModelForm):
    class Meta:
        model = SeoExtension.twitter_meta.through
        fields = "__all__"

    def __str__(self):
        return str(self.instance.twittercardmeta)
