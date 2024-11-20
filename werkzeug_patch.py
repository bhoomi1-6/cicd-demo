# werkzeug_patch.py
from urllib.parse import quote as url_quote
from urllib.parse import urlparse as url_parse

# Apply the patch
import werkzeug.urls
werkzeug.urls.url_quote = url_quote
werkzeug.urls.url_parse = url_parse
