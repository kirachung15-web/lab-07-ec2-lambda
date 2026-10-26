import logging

from chalice import Chalice
from chalicelib.analyze import analyze_book

BUCKET = "public-xda8uy"

app = Chalice(app_name="book-analyzer")
logging.getLogger().setLevel(logging.INFO)


@app.on_s3_event(bucket=BUCKET, events=["s3:ObjectCreated:*"], suffix=".txt")
def analyze_new_book(event):
    """Analyze a book when it is uploaded to S3."""
    analyze_book(event.bucket, event.key)
