# werkzeug_patch.py
from urllib.parse import quote as url_quote

# Apply the patch
import werkzeug.urls
werkzeug.urls.url_quote = url_quote
