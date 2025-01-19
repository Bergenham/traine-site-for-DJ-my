from django.contrib.sitemaps import Sitemap
from .models import Article

class BlogSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Article.objects.filter(p_d__isnull=False).order_by('-p_d')

    def lastmod(self, obj: Article):
        return obj.p_d

    # def item_link(self, item: Article):
    #     return reverse('blogapp:detail_blog', kwargs={'pk': item.pk})