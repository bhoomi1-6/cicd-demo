# werkzeug_patch.py
from urllib.parse import quote as url_quote
from urllib.parse import urlparse as url_parse

# Apply the patch
import werkzeug.urls
werkzeug.urls.url_quote = url_quote
werkzeug.urls.url_parse = url_parse
# Add the `__version__` attribute if missing
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "2.0.3"  # Set to a compatible version
